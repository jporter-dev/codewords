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

REDIS_TTL_S = 60*10 if os.environ.get('FLASK_DEV', False) else  60*60*12
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
    games = {}
    for k in db.scan_iter():
        gm = get_game(k)
        games[gm.game_id] = {
            "last_modified": gm.date_modified,
            "playtime_m": gm.playtime(),
            "last_turn_m": round((datetime.now() - gm.date_modified).total_seconds() / 60, 2)
        }
    games = dict(sorted(games.items(), key=lambda x: x[1]['last_turn_m'], reverse=True))
    resp = {
        "total": db.dbsize(),
        "games": games
    }
    return jsonify(resp)

@socketio.on('disconnect')
def on_disconnect():
    for room in rooms(sid=request.sid):
        gm = get_game(room)
        if gm:
            join_room(room)
            gm.players.remove(request.sid)
            send(gm.to_json(), room=room)
            save_game(gm)

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

    gm.players.add(request.sid, data.get('username', None))
    # write room to redis
    join_room(gm.game_id)
    # rooms[room].add_player(username)
    emit('join_room', {'room': gm.game_id})
    save_game(gm)

@socketio.on('join')
def on_join(data):
    """Join a game lobby"""
    room = data['room']
    gm = get_game(room)
    # send(request.sid, room=room)
    if gm:
        # add player and rebroadcast game object
        join_room(room)
        gm.players.add(request.sid, data.get('username', None))
        send(gm.to_json(), room=room)
        save_game(gm)

@socketio.on('toggle_spymaster')
def on_toggle_spymaster(data):
    """flip card and rebroadcast game object"""
    gm = get_game(data['room'])
    if (request.sid in gm.players.spymasters and not data['state']) or (request.sid not in gm.players.spymasters and data['state']):
        gm.players.toggle_spymaster(request.sid, data['state'])
        send(gm.to_json(), room=data['room'])
        save_game(gm)

@socketio.on('flip_card')
def on_flip_card(data):
    """flip card and rebroadcast game object"""
    room = data['room']
    gm = get_game(room)
    gm.flip_card(data['card'])
    send(gm.to_json(), room=room)
    save_game(gm)

@socketio.on('regenerate')
def on_regenerate(data):
    """regenerate the words list"""
    room = data['room']
    gm = get_game(room)
    gm.generate_board(data.get('newGame', False))
    send(gm.to_json(), room=room)
    save_game(gm)

@socketio.on('list_dictionaries')
def list_dictionaries():
    """send a list of dictionary names"""
    # send dict list to client
    emit('list_dictionaries', game.DICTIONARIES)

@socketio.on('test')
def test():
    """send a list of dictionary names"""
    # send dict list to client
    emit('test', "ack")

def get_game(room):
    gm = db.get(room)
    if gm:
        return pickle.loads(gm)
    else:
        emit('error', {'error': 'Unable to join room ['+ room +']. Room does not exist.'})
        return None

def save_game(game):
    db.setex(game.game_id, REDIS_TTL_S, pickle.dumps(game))

def exit_handler():
    for room in db.keys():
        gm = get_game(room)
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
