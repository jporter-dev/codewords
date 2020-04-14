"""Flask server for Codenames"""
# pylint: disable=C0103

import eventlet
import logging
import pickle
import redis
import json
import os
import gc
from datetime import timedelta
from sys import getsizeof
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, join_room, leave_room, close_room, send, emit
from datetime import datetime, timedelta
from functools import reduce
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from codenames import game
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

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    # username = data['username']
    # create the game
    # handle custom wordbanks
    if data['dictionaryOptions']['useCustom']:
        gm = game.Info(
            size=data['size'],
            teams=data['teams'],
            wordbank=data['dictionaryOptions']['customWordbank'])
    # dict mixer
    elif data['dictionaryOptions']['mix']:
        gm = game.Info(
            size=data['size'],
            teams=data['teams'],
            mix=data['dictionaryOptions']['mixPercentages'])

    # handle standard single dictionary
    else:
        gm = game.Info(
            size=data['size'],
            teams=data['teams'],
            dictionary=data['dictionaryOptions']['dictionaries'])

    room = gm.game_id
    # write room to redis
    db.setex(room, REDIS_TTL_S, pickle.dumps(gm))

    join_room(room)
    # rooms[room].add_player(username)
    emit('join_room', {'room': room})

@socketio.on('join')
def on_join(data):
    """Join a game lobby"""
    # username = data['username']
    # print(request.sid)
    room = data['room']
    gm = get_game(room)
    # send(request.sid, room=room)
    if gm:
        # add player and rebroadcast game object
        # rooms[room].add_player(username)
        join_room(room)
        send(gm.to_json(), room=room)

@socketio.on('flip_card')
def on_flip_card(data):
    """flip card and rebroadcast game object"""
    room = data['room']
    gm = get_game(room)
    gm.flip_card(data['card'])
    db.setex(room, REDIS_TTL_S, pickle.dumps(gm))
    send(gm.to_json(), room=room)

@socketio.on('regenerate')
def on_regenerate(data):
    """regenerate the words list"""
    room = data['room']
    gm = get_game(room)
    gm.generate_board(data.get('newGame', False))
    db.setex(room, REDIS_TTL_S, pickle.dumps(gm))
    send(gm.to_json(), room=room)

@socketio.on('list_dictionaries')
def list_dictionaries():
    """send a list of dictionary names"""
    # send dict list to client
    emit('list_dictionaries', game.DICTIONARIES)

def get_game(room):
    gm = db.get(room)
    if gm:
        return pickle.loads(gm)
    else:
        emit('error', {'error': 'Unable to join room ['+ room +']. Room does not exist.'})
        return None

if __name__ == '__main__':
    use_reloader = False
    if os.environ.get('FLASK_DEV', False):
        app.config['DEBUG'] = True
        use_reloader = True

    app.config['JSON_SORT_KEYS'] = False
    app.config['DEBUG'] = os.environ.get('DEBUG', False)
    socketio.run(app, host='0.0.0.0', use_reloader=use_reloader)
