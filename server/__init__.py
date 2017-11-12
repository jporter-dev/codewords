from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask_bootstrap import Bootstrap, StaticCDN
from codenames import game
import eventlet
import random
import string

eventlet.monkey_patch()

app = Flask(__name__)
Bootstrap(app)
socketio = SocketIO(app)
app.extensions['bootstrap']['cdns']['jquery'] = StaticCDN()
app.extensions['bootstrap']['cdns']['bootstrap'] = StaticCDN()
app.secret_key = b'FF\x90}\xdc\xc5\xaeaT\xd6\xbc\x86O\xa6B\xdd\xa2qp\x9e\xd2f\xe8\xe8'

rooms = {}

# main index. serves up built HTML from webpack
@app.route('/')
def index():
    return render_template('index.html')

# display room stats
@app.route('/purge')
def purge():
    purged = rooms.keys()
    rooms.clear()
    return jsonify({
        "purged": purged,
        "total": len(rooms.items())
    })

# display room stats
@app.route('/stats')
def stats():
    resp = {
        "total": len(rooms.items())
    }
    if 'rooms' in request.args:
        resp["rooms"] = {k: v.to_json() for k, v in rooms.items()}
    return jsonify(resp)

# BEGIN CODENAMESv2 -- WEBSOCKETS
# required params

# create a game
# generate the cards and starting team
# params: 
#   card deck
#   board size
#   # of teams - v2.1?
@socketio.on('create')
def on_create(data):
    # username = data['username']
    # create the room
    id_length = 5
    room = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(id_length))
    join_room(room)
    # create the game
    rooms[room] = game.Info(game_id=room, size=data['size'], teams=data['teams'], dictionary=data['dictionary'])
    # rooms[room].add_player(username)
    emit('join_room', {'room': room})

# join a game
@socketio.on('join')
def on_join(data):
    # username = data['username']
    room = data['room']
    if room in rooms:
        # add player and rebroadcast game object
        # rooms[room].add_player(username)
        join_room(room)
        send(rooms[room].to_json(), room=room)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist.'})

# leave a game
@socketio.on('leave')
def on_leave(data):
    # username = data['username']
    room = data['room']
    # add player and rebroadcast game object
    # rooms[room].remove_player(username)
    leave_room(room)
    send(rooms[room].to_json(), room=room)

# take a turn
@socketio.on('flip_card')
def on_flip_card(data):
    # flip card and rebroadcast game object
    room = data['room']
    card = data['card']
    rooms[room].flip_card(card)
    send(rooms[room].to_json(), room=room)

# set spymaster

if __name__ == '__main__':
    #app.add_url_rule('/favicon.ico',redirect_to=url_for('static', filename='favicon.ico'))                                                                                                                          
    # app.run(host='0.0.0.0', debug=True)
    socketio.run(app, host='0.0.0.0', debug=True)


