"""Object for tracking game status"""
from datetime import datetime
import time
import random
import math
import string
import os

# dictionaries
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
FILE_ROOT = os.path.join(APP_ROOT, '..', 'dictionaries')

DICTIONARIES = {}
DICTIONARIES["English"] =                   FILE_ROOT + "/english.txt"
DICTIONARIES["Czech"] =                     FILE_ROOT + "/czech.txt"
DICTIONARIES["French"] =                    FILE_ROOT + "/french.txt"
DICTIONARIES["German"] =                    FILE_ROOT + "/german.txt"
DICTIONARIES["Greek"] =                     FILE_ROOT + "/greek.txt"
DICTIONARIES["Italian"] =                   FILE_ROOT + "/italian.txt"
DICTIONARIES["Portuguese"] =                FILE_ROOT + "/portuguese.txt"
DICTIONARIES["Russian"] =                   FILE_ROOT + "/Russian.txt"
DICTIONARIES["Spanish"] =                   FILE_ROOT + "/Spanish.txt"
DICTIONARIES["Cards Against Humanity"] =    FILE_ROOT + "/cards_against_humanity.txt"

# colors per team
RED = 'R'
BLUE = 'B'
GREEN = 'G'
# num words per board
BOARD_SIZE = {
    'normal': 25,
    'large': 81
}
BIG_BLACKOUT_SPOTS = [4, 20, 24, 36, 40, 44, 56, 60, 76]

class Info(object):
    # pylint: disable=too-many-instance-attributes
    """Object for tracking game stats"""
    def __init__(self, dictionary='English', size='normal', teams=2, wordbank=False, mix=False):
        self.wordbank = wordbank
        self.game_id = self.generate_room_id()
        self.starting_color = RED
        self.date_created = datetime.now()
        self.date_modified = self.date_created
        self.players = []
        self.size = size
        self.teams = teams
        self.dictionary = dictionary
        self.mix = mix
        self.dictionaries = DICTIONARIES.keys()
        self.minWords = BOARD_SIZE[self.size]

        # gererate board
        self.generate_board()

    def to_json(self):
        """Serialize object to JSON"""
        return {
            "game_id": self.game_id,
            "starting_color": self.starting_color,
            "players": self.players,
            "date_created": str(self.date_created),
            "date_modified": str(self.date_modified),
            "playtime": self.playtime(),
            "board": self.board,
            "solution": self.solution,
            "options": {
                "dictionary": self.dictionary,
                "size": self.size,
                "teams": self.teams,
                "mix": self.mix,
                "custom": self.wordbank
            },

        }

    def generate_board(self, newGame=False):
        """Generate a list of words"""
        # remove current words from bank if newGame and not shuffle
        if newGame and hasattr(self, 'words') and (self.wordbank and len(self.wordbank) - self.minWords >= self.minWords):
            for word in self.words:
                self.wordbank.remove(word)
        self.words = self.__get_words(self.size)
        self.layout = self.__get_layout(self.size, int(self.teams))
        self.board = dict.fromkeys(self.words, False)
        self.solution = dict(zip(self.words, self.layout))

    def flip_card(self, word):
        """Assign color to card in solution dict"""
        self.date_modified = datetime.now()
        if word not in self.words:
            return 'Invalid word entered.'
        self.board[word] = self.solution[word]
        return self.solution[word]

    def add_player(self, name):
        """Add playername to player array"""
        self.players.append(name)

    def remove_player(self, name):
        """Remove playername to player array"""
        self.players.remove(name)

    @classmethod
    def generate_room_id(cls):
        """Generate a random room ID"""
        id_length = 5
        return ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(id_length))

    def playtime(self):
        # 2018-08-12 10:12:25.700528
        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = self.date_created
        d2 = self.date_modified
        # Convert to Unix timestamp
        d1_ts = time.mktime(d1.timetuple())
        d2_ts = time.mktime(d2.timetuple())
        return round(float(d2_ts-d1_ts) / 60, 2)

    def __get_words(self, size):
        """Generate a list of words"""
        if not self.dictionary in DICTIONARIES.keys():
            print("Error: dictionary '" + self.dictionary + "' doesn't exist")
            return None
        # override words with the wordbank
        words = self.wordbank
        if not self.wordbank:
            if self.mix:
                words = []
                for key in self.mix:
                    # load and shuffle current dict
                    tempWords = self.__load_words(key)
                    random.shuffle(tempWords)
                    # get word ratio (rounded up)
                    numWords = int(math.ceil((self.mix[key]/100.0)*BOARD_SIZE[size]))
                    words = words + tempWords[0:numWords]
            else:
                words = self.__load_words(self.dictionary)
        random.shuffle(words)
        final_words = words[0:BOARD_SIZE[size]]
        return final_words

    def __load_words(self, d):
        with open(DICTIONARIES.get(d), 'r') as words_file:
            return [elem for elem in words_file.read().split('\n') if len(elem.strip()) > 0]

    def __get_layout(self, size, teams):
        """Randomly generate a card layout"""
        size = BOARD_SIZE[size]
        self.starting_color = RED
        green = 0
        # normal board size
        if size == BOARD_SIZE['normal']:
            if teams == 3:
                blue = 5
                red = 5
                green = 5
            else:
                blue = 8
                red = 8

            bystanders = size - blue - red - green - 2
        # large board size
        else:
            if teams == 2:
                blue = 8
                red = 8
            elif teams == 3:
                blue = 8
                red = 8
                green = 8
            num_blackouts = 9
            bystanders = size - num_blackouts - blue - red - green - 3
        # if 2 teams, pick a starting team
        if teams == 2:
            if random.random() < 0.5:
                blue += 1
                self.starting_color = BLUE
            else:
                red += 1
        # if 3 teams, pick a starting team
        else:
            if random.random() < 0.333:
                blue += 1
                self.starting_color = BLUE
            elif random.random() > 0.666:
                green += 1
                self.starting_color = GREEN
            else:
                red += 1

        mix = ["B"] * blue
        mix.extend(["R"] * red)
        if green > 0:
            mix.extend(['G'] * green)
        mix.extend(["X"])
        if size == BOARD_SIZE['large']:
            mix.extend(['X'])
        mix.extend(["O"] * bystanders)
        random.shuffle(mix)
        if size == BOARD_SIZE['large']:
            for i in BIG_BLACKOUT_SPOTS:
                mix.insert(i, '-')
        return mix
