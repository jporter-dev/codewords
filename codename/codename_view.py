import random
import socket
from codename import codename_game_info as game_info


HOME_CAH_FILE="/home/daniel/development/projects/sprek/codenames/cah_code_names.txt"
HOME_POP_CULTURE_FILE="/home/daniel/development/projects/sprek/codenames/code_names_pop.txt"
HOME_DICTIONARY_FILE="/home/daniel/development/projects/sprek/codenames/code_names_dict.txt"
HOME_SIMPLE_FILE="/home/daniel/development/projects/sprek/codenames/code_names_simple.txt"
SERVER_CAH_FILE="/home/sprek/cah_code_names.txt"
SERVER_POP_CULTURE_FILE="/home/sprek/code_names_pop.txt"
SERVER_DICTIONARY_FILE="/home/sprek/code_names_dict.txt"
SERVER_SIMPLE_FILE="/home/sprek/code_names_simple.txt"

FILE_LOOKUP_HOME={"CAH" : HOME_CAH_FILE, "Pop Culture" : HOME_POP_CULTURE_FILE, "Dictionary" : HOME_DICTIONARY_FILE, "Simple" : HOME_SIMPLE_FILE}
FILE_LOOKUP_SERVER={"CAH" : SERVER_CAH_FILE, "Pop Culture" : SERVER_POP_CULTURE_FILE, "Dictionary" : SERVER_DICTIONARY_FILE, "Simple" : SERVER_SIMPLE_FILE}

red_color = '#df2020'
blue_color= '#207fdf'
black_color= '#505050'
green_color = '#33cc33'
white_color= '#cccccc'

blackout_color= '#000000'

SIZE_TYPE_NORMAL='normal'
SIZE_TYPE_BIG='big'

NUM_WORDS_NORMAL=25
NUM_WORDS_BIG=81

BIG_BLACKOUT_SPOTS=[4,20,24,36,40,44,56,60,76]

def get_dict_path(file_lookup):
    cur_host = socket.gethostname()
    if 'webfaction' in cur_host:
        return FILE_LOOKUP_SERVER[file_lookup]
    return FILE_LOOKUP_HOME[file_lookup]

def get_color(char):
    if char == 'R':
        return red_color
    elif char == 'B':
        return blue_color
    elif char == 'G':
        return green_color
    elif char == 'X':
        return black_color
    elif char == '-':
        return blackout_color
    else:
        return white_color

def get_player_info(dictionary, num_words=NUM_WORDS_NORMAL):
    if not dictionary in FILE_LOOKUP_SERVER.keys():
        print ("Error: dictionary '" + dictionary + "' doesn't exist")
        return None
    words_file = open(get_dict_path(dictionary), 'r')
    words = [elem for elem in words_file.read().split('\n') if len(elem.strip()) > 0]
    random.shuffle(words)
    final_words = words[0:num_words]
    return final_words
    
def get_game_info(size=SIZE_TYPE_NORMAL, players=2):
    ginfo = game_info.GameInfo()
    ginfo.game_id = 0
    ginfo.adv_color = game_info.RED
    green=0
    if size == SIZE_TYPE_NORMAL:
        if players==3:
            blue = 5
            red = 5
            green = 5
        else:
            blue = 8
            red = 8

        bystanders = 25 - blue - red - green - 2
    else:
        if players == 2:
            blue = 8
            red = 8
        elif players == 3:
            blue = 8
            red = 8
            green = 8
        num_blackouts = 9
        bystanders = 81 - num_blackouts - blue - red - green - 3
    if players == 2:
        if random.random() < 0.5:
            blue += 1
            ginfo.adv_color = game_info.BLUE
        else:
            red += 1
    else:
        if random.random() < 0.333:
            blue += 1
            ginfo.adv_color = game_info.BLUE
        elif random.random() > 0.666:
            green += 1
            ginfo.adv_color = game_info.GREEN
        else:
            red += 1
    mix = ["B"] * blue
    mix.extend(["R"] * red)
    if green > 0:
        mix.extend(['G'] * green)
    mix.extend(["X"])
    if size == SIZE_TYPE_BIG:
        mix.extend(['X'])
    mix.extend(["O"] * bystanders)
    random.shuffle(mix)
    if size == SIZE_TYPE_BIG:
        for i in BIG_BLACKOUT_SPOTS:
            mix.insert(i, '-')
    ginfo.layout = mix
    return ginfo
    
def get_leader_html(seed=None, size=SIZE_TYPE_NORMAL, players=2):
    if seed:
        random.seed(seed)
    html = ''
    ginfo = get_game_info(size, players)
    color_text = "Red"
    if ginfo.adv_color == game_info.BLUE:
        color_text = "Blue"
    elif ginfo.adv_color == game_info.GREEN:
        color_text = "Green"
    count = 0
    html += '<h3 style="color: ' + get_color(ginfo.adv_color) + '">' + color_text + ' starts</h3>'
    if size == SIZE_TYPE_NORMAL:
        html += "<table style='width: 500px; height: 500px'>"
        for r in range (0,5):
            html += "<tr>"
            for c in range (0,5):
                html += "<td style=\"border: 1px solid black; padding: 20px; background: " + get_color(ginfo.layout[count]) + ";\">&nbsp;&nbsp;&nbsp;</td>"
                count += 1
            html += "</tr>"
        html += "</table>"
    elif size == SIZE_TYPE_BIG:
        html += "<table style='width: 1000px; height: 1000px'>"
        for r in range (0,9):
            html += "<tr>"
            for c in range (0,9):
                html += "<td style=\"border: 1px solid black; padding: 20px; background: " + get_color(ginfo.layout[count]) + ";\">&nbsp;&nbsp;&nbsp;</td>"
                
                count += 1
            html += "</tr>"
        html += "</table>"
    
    return html

def get_game_html(dictionary,seed=None, size=SIZE_TYPE_NORMAL):
    if seed:
        random.seed(seed)
    html = ''
    count = 0
    html += "<table style='table-layout: fixed; width: 100%; height: 100%'>"
    #html += "<table style='table-layout: fixed; width: 800px; height: 600px'>"
    num_words = NUM_WORDS_NORMAL
    if size == SIZE_TYPE_BIG:
        num_words = NUM_WORDS_BIG
    words = get_player_info(dictionary, num_words)
    if size == SIZE_TYPE_NORMAL:
        for r in range (0,5):
            html += "<tr>"
            for c in range (0,5):
                html += "<td class='codename_cell' id='cell_"+str(r)+str(c)+"'style=\"padding: 5px; border: 1px solid black; background: " + white_color + "; font-size: 100%; text-align: center\">" + words[count] +"</td>"
                count += 1
            html += "</tr>"
        html += "</table></br>"
    elif size == SIZE_TYPE_BIG:
        for r in range (0,9):
            html += "<tr>"
            for c in range (0,9):
                if 9*r+c in BIG_BLACKOUT_SPOTS:
                    html += "<td class='codename_cell' id='cell_"+str(r)+str(c)+"'style=\"padding: 5px; border: 1px solid black; background: " + blackout_color + "; font-size: 100%; text-align: center\"></td>"
                else:
                    html += "<td class='codename_cell' id='cell_"+str(r)+str(c)+"'style=\"padding: 5px; border: 1px solid black; background: " + white_color + "; font-size: 100%; text-align: center\">" + words[count] +"</td>"
                count += 1
            html += "</tr>"
        html += "</table></br>"
    return html
