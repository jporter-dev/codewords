from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap, StaticCDN
from codename import codename_view
import socket
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


@app.route('/')
def index():
    return render_template('index.html')


# --------------------------------------------------                                                                                                                                                                 
# codename                                                                                                                                                                                                           

@app.route('/codename')
def codename():
    return render_template('codename/codename.html')

@app.route('/codename/leader')
def leader():
    return render_template('codename/leader.html', code_html=codename_view.get_leader_html())

@app.route('/codename/set_seed_leader', methods=('POST','GET'))
def set_seed_leader():
    seed=int(request.form["seed_input"].strip())
    size=request.form["size_select"].strip()
    players=request.form["players_select"].strip()
    players=int(players)
    return codename_view.get_leader_html(seed, size, players)

@app.route('/codename/set_seed_game', methods=('POST','GET'))
def set_seed_game():
    seed = None
    if request.form["seed_input"]:
        seed=int(request.form["seed_input"].strip())
    dict_select=request.form["dict_select"].strip()
    size=request.form["size_select"].strip()
    
    return codename_view.get_game_html(dict_select,seed,size)

@app.route('/codename/play')
def play():
    return render_template('codename/play.html', code_html=codename_view.get_game_html("Dictionary", size='normal'))

if __name__ == '__main__':
    #app.add_url_rule('/favicon.ico',redirect_to=url_for('static', filename='favicon.ico'))                                                                                                                          
    # app.run(host='0.0.0.0', debug=True)
    socketio.run(app, host='0.0.0.0', debug=True)


