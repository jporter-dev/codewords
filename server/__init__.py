"""Flask server for Codenames"""
# pylint: disable=C0103

import eventlet
import logging
import json
import os
import gc
from sys import getsizeof
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from datetime import datetime, timedelta
from functools import reduce
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from dotenv import load_dotenv
load_dotenv()

# attempt a relative import
try:
    from .codenames import game
except (ImportError, ValueError):
    from codenames import game

# init sentry
sentry_dsn = os.getenv("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()]
    )

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = os.getenv("SECRET_KEY", "")

# set up logging
if not app.debug:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

ROOMS = {}

@app.route('/prune')
def prune():
    global ROOMS
    """Prune rooms stale for more than 6 hours"""
    total = 0
    if ROOMS:
        total = len(ROOMS.keys())
        # get stale rooms (delta between now and date_modified >= defined stale_delta_s)
        stale_delta_s = 21600
        stale = [v.to_json() for v in ROOMS.values() if (datetime.now() -
            datetime.strptime(
                v.to_json().get('date_modified'),'%Y-%m-%d %H:%M:%S.%f'
            )).total_seconds() >= stale_delta_s]
        if len(stale) > 0:
            cur_path = os.path.dirname(os.path.abspath(__file__))
            # add playtimes to master playtimes list
            with open(os.path.join(cur_path, 'all-playtimes.txt'), 'a+') as f:
                playtimes = [json.dumps([v['date_created'], v['playtime']])
                    for v in sorted(stale, key=lambda k: k.get('date_modified'))
                    if v['playtime'] > 10]
                f.write("\r\n".join(playtimes))
                del playtimes
            # add custom words to master list
            with open(os.path.join(cur_path, 'all-custom-words.txt'), 'a+') as f:
                custom_words = [json.dumps(v['options']['custom'])
                for v in stale if v['options']['custom'] is not False]
                f.write("\r\n".join(custom_words))
                del custom_words
            # prune master rooms list
            for game in stale:
                del ROOMS[game.get('game_id')]
            gc.collect()
    return jsonify({
        "pruned": total - len(ROOMS.keys())
    })

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

@app.route('/stats')
def stats():
    """display room stats"""
    resp = {
        "total": len(ROOMS.keys()),
        "bytes_used": getsizeof(ROOMS)
    }
    if 'rooms' in request.args:
        if ROOMS:
            resp["rooms"] = sorted([ v.to_json() for v in ROOMS.values() ], key=lambda k: k.get('date_modified'), reverse=True)
        else:
            resp["rooms"] = None
    return jsonify(resp)

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    # username = data['username']
    # create the game
    # handle custom wordbanks
    global ROOMS
    # prune old rooms
    prune()
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
    ROOMS[room] = gm
    join_room(room)
    # rooms[room].add_player(username)
    emit('join_room', {'room': room})

@socketio.on('join')
def on_join(data):
    """Join a game lobby"""
    # username = data['username']
    room = data['room']
    if room in ROOMS:
        # add player and rebroadcast game object
        # rooms[room].add_player(username)
        join_room(room)
        send(ROOMS[room].to_json(), room=room)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist.'})

@socketio.on('leave')
def on_leave(data):
    """Leave the game lobby"""
    # username = data['username']
    room = data['room']
    # add player and rebroadcast game object
    # rooms[room].remove_player(username)
    leave_room(room)
    send(ROOMS[room].to_json(), room=room)

@socketio.on('flip_card')
def on_flip_card(data):
    """flip card and rebroadcast game object"""
    room = data['room']
    card = data['card']
    ROOMS[room].flip_card(card)
    send(ROOMS[room].to_json(), room=room)

@socketio.on('regenerate')
def on_regenerate(data):
    """regenerate the words list"""
    room = data['room']
    ROOMS[room].generate_board(data.get('newGame', False))
    send(ROOMS[room].to_json(), room=room)

@socketio.on('list_dictionaries')
def list_dictionaries():
    """send a list of dictionary names"""
    # send dict list to client
    emit('list_dictionaries', {'dictionaries': list(game.DICTIONARIES.keys())})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
