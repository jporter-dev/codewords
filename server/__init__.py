from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask_bootstrap import Bootstrap, StaticCDN
from codenames import game
import random
import string

app = Flask(__name__)
Bootstrap(app)
socketio = SocketIO(app)
app.extensions['bootstrap']['cdns']['jquery'] = StaticCDN()
app.extensions['bootstrap']['cdns']['bootstrap'] = StaticCDN()
app.secret_key = b'FF\x90}\xdc\xc5\xaeaT\xd6\xbc\x86O\xa6B\xdd\xa2qp\x9e\xd2f\xe8\xe8'

rooms = {}

# sprek's homepage
@app.route('/')
def index():
    return render_template('index.html')

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
    username = data['username']
    # create the room
    id_length = 5
    room = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(id_length))
    join_room(room)
    # create the game
    rooms[room] = game.Info(game_id=room)
    rooms[room].add_player(username)
    emit('join_room', {'room': room})

# join a game
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    # add player and rebroadcast game object
    rooms[room].add_player(username)
    join_room(room)
    send(rooms[room].to_json(), room=room)

# leave a game
@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    # add player and rebroadcast game object
    rooms[room].remove_player(username)
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


