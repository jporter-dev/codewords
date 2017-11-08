from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from flask_bootstrap import Bootstrap, StaticCDN
from codename import codename_view
import socket
import random
import string
import json
import logging
import logging.handlers

app = Flask(__name__)
Bootstrap(app)
socketio = SocketIO(app)
app.extensions['bootstrap']['cdns']['jquery'] = StaticCDN()
app.extensions['bootstrap']['cdns']['bootstrap'] = StaticCDN()
app.secret_key = b'FF\x90}\xdc\xc5\xaeaT\xd6\xbc\x86O\xa6B\xdd\xa2qp\x9e\xd2f\xe8\xe8'

LOG_FILENAME='/home/sprek/logs/user/flask_webapp.log'

cur_host = socket.gethostname()
if 'webfaction' in cur_host:
    file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5242880, backupCount=10)
    app.logger.addHandler(file_handler)

# sprek's homepage
@app.route('/')
def index():
    return render_template('index.html')


# --------------------------------------------------                                                                                                                                                                 
# codename                                                                                                                                                                                                          

# codenames landing page
# choose player role [leader, player]
@app.route('/codename')
def codename():
    return render_template('codename/codename.html')

# leader view
@app.route('/codename/leader')
def leader():
    return render_template('codename/leader.html', code_html=codename_view.get_leader_html())

# REST endpoint to set leader seed
@app.route('/codename/set_seed_leader', methods=('POST','GET'))
def set_seed_leader():
    seed=int(request.form["seed_input"].strip())
    size=request.form["size_select"].strip()
    players=request.form["players_select"].strip()
    players=int(players)
    return codename_view.get_leader_html(seed, size, players)

# REST endpoint to set player seed
@app.route('/codename/set_seed_game', methods=('POST','GET'))
def set_seed_game():
    seed = None
    if request.form["seed_input"]:
        seed=int(request.form["seed_input"].strip())
    dict_select=request.form["dict_select"].strip()
    size=request.form["size_select"].strip()
    
    return codename_view.get_game_html(dict_select,seed,size)

# player view
@app.route('/codename/play')
def play():
    return render_template('codename/play.html', code_html=codename_view.get_game_html("Dictionary", size='normal'))


# BEGIN CODENAMESv2 -- WEBSOCKETS
# Actions:
#   Create a lobby [deck, size] - this will generate a random seed for others to join with
#   Join the lobby using seed from above
#   Leave the lobby
#   Get cards - probably can be sent with the "on join" event as an initializer
#       This will have to vary based on leader/player
#   Select and validate a card - this will update all players
# TODOS for existing architecture
#   Convert calls to return JSON instead of HTML and templates

@socketio.on('create')
def on_create(data):
    id_length = 5
    room = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(id_length))
    username = data['username']
    join_room(room)
    send(username + ' has created the room. [' + room + ']')
    emit('room_created', {"room": room})

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    print(data)
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)

# @socketio.on('')

if __name__ == '__main__':
    #app.add_url_rule('/favicon.ico',redirect_to=url_for('static', filename='favicon.ico'))                                                                                                                          
    # app.run(host='0.0.0.0', debug=True)
    socketio.run(app, host='0.0.0.0', debug=True)


