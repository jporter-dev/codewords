"""Flask server for Codenames"""
# pylint: disable=C0103

import eventlet
import logging
import pickle
import redis
import atexit
import json
import os
import gc
from datetime import timedelta
from sys import getsizeof
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, join_room, leave_room, close_room, send, emit, rooms
from datetime import datetime, timedelta
from functools import reduce
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from codenames import game, players
from dotenv import load_dotenv
load_dotenv()

ACTIVE_CLIENTS = 0
# TTL is 10m in dev, 12h in prod
REDIS_TTL_S = 60*10 if os.environ.get('FLASK_DEV', False) else  60*60*12
GAME_NAMESPACE = 'game/'
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.secret_key = os.getenv("SECRET_KEY", "codenames")
db = redis.Redis(host='redis', port=6379, db=0)

# init sentry
sentry_dsn = os.getenv("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()]
    )

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

@app.route('/stats')
def stats():
    """display room stats"""
    resp = {
        "active_clients": ACTIVE_CLIENTS,
        "active_games": len(db.keys(GAME_NAMESPACE + '*'))
    }

    if request.args.get('g') is not None:
        games = {}
        for k in db.scan_iter(GAME_NAMESPACE + '*'):
            gm = get_game(k, False)
            games[gm.game_id] = {
                "last_modified": gm.date_modified,
                "playtime_m": gm.playtime(),
                "last_turn_m": round((datetime.now() - gm.date_modified).total_seconds() / 60, 2),
                "dictionary": gm.dictionary,
                "custom": bool(gm.wordbank),
                "total_players": len(gm.players.all_players),
                "all_players":  list(gm.players.all_players),
                "current_players": list(gm.players.players.values())
            }
        games = dict(sorted(games.items(), key=lambda x: x[1]['last_turn_m']))
        resp['all_games'] = games
    return jsonify(resp)

@socketio.on('connect')
def on_connect():
    global ACTIVE_CLIENTS
    ACTIVE_CLIENTS += 1
    emit('list_dictionaries', game.DICTIONARIES)

@socketio.on('disconnect')
def on_disconnect():
    global ACTIVE_CLIENTS
    ACTIVE_CLIENTS -= 1
    for room in rooms(sid=request.sid):
        gm = get_game(room)
        if gm:
            join_room(room)
            gm.players.remove(request.sid)
            save_game(gm)
            send(gm.to_json(), room=room)

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    # username = data['username']
    # create the game
    # handle custom wordbanks
    if data['dictionaryOptions']['useCustom']:
        gm = game.Game(
            size=data['size'],
            teams=data['teams'],
            wordbank=data['dictionaryOptions']['customWordbank'])
    # dict mixer
    elif data['dictionaryOptions']['mix']:
        gm = game.Game(
            size=data['size'],
            teams=data['teams'],
            mix=data['dictionaryOptions']['mixPercentages'])

    # handle standard single dictionary
    else:
        gm = game.Game(
            size=data['size'],
            teams=data['teams'],
            dictionary=data['dictionaryOptions']['dictionaries'])

    # add current user to players list
    gm.players.add(request.sid, data.get('username', None))

    # check if ID exists
    while(get_game(gm.game_id) is not None):
        gm.regenerate_id()

    # write room to redis
    join_room(gm.game_id)
    save_game(gm)
    emit('join_room', {'room': gm.game_id})

@socketio.on('join')
def on_join(data):
    """Join a game lobby"""
    room = data['room']
    gm = get_game(room)
    if gm:
        # add player and rebroadcast game object
        join_room(room)
        gm.players.add(request.sid, data.get('username', None))
        save_game(gm)
        send(gm.to_json(), room=room)

@socketio.on('leave')
def on_leave(data):
    """Join a game lobby"""
    room = data['room']
    gm = get_game(room)
    if gm:
        # remove player and rebroadcast game object
        leave_room(room)
        gm.players.remove(request.sid)
        save_game(gm)
        send(gm.to_json(), room=room)

@socketio.on('close_room')
def on_close_room(data):
    """Join a game lobby"""
    db.delete(GAME_NAMESPACE + data['room'])
    close_room(data['room'])
    emit('error', {'error': 'Unable to join, room does not exist.'})

@socketio.on('toggle_spymaster')
def on_toggle_spymaster(data):
    """flip card and rebroadcast game object"""
    gm = get_game(data['room'])
    if (gm):
        if (request.sid in gm.players.spymasters and not data['state']) or (request.sid not in gm.players.spymasters and data['state']):
            gm.players.toggle_spymaster(request.sid, data['state'])
        save_game(gm)
        send(gm.to_json(), room=data['room'])

@socketio.on('flip_card')
def on_flip_card(data):
    """flip card and rebroadcast game object"""
    room = data['room']
    gm = get_game(room)
    gm.flip_card(data['card'])
    save_game(gm)
    emit("resetTimer", room=room)
    send(gm.to_json(), room=room)

@socketio.on('regenerate')
def on_regenerate(data):
    """regenerate the words list"""
    room = data['room']
    gm = get_game(room)
    gm.generate_board(data.get('newGame', False))
    if data.get('newGame') is True:
        gm.players.reset_spymasters()
    save_game(gm)
    send(gm.to_json(), room=room)

@socketio.on('list_dictionaries')
def list_dictionaries():
    """send a list of dictionary names"""
    # send dict list to client
    emit('list_dictionaries', game.DICTIONARIES)

@socketio.on('start_timer')
def start_timer(data):
    emit("startTimer", room=data['room'])

@socketio.on('pause_timer')
def pause_timer(data):
    emit("pauseTimer", room=data['room'])

@socketio.on('reset_timer')
def reset_timer(data):
    emit("resetTimer", room=data['room'])


def get_game(room, prefix=True):
    room = GAME_NAMESPACE + room if prefix else room
    gm = db.get(room)
    if gm:
        return pickle.loads(gm)
    else:
        emit('error', {'error': 'Unable to join, room does not exist.'})
        return None

def save_game(game):
    db.setex(GAME_NAMESPACE + game.game_id, REDIS_TTL_S, pickle.dumps(game))

def exit_handler():
    for room in db.keys(GAME_NAMESPACE + '*'):
        gm = get_game(room, False)
        gm.players.reset()
        save_game(gm)

if __name__ == '__main__':
    use_reloader = False
    if os.environ.get('FLASK_DEV', False):
        app.config['DEBUG'] = True
        use_reloader = True

    app.config['JSON_SORT_KEYS'] = False
    app.config['DEBUG'] = os.environ.get('DEBUG', False)

    atexit.register(exit_handler)

    socketio.run(app, host='0.0.0.0', use_reloader=use_reloader)
