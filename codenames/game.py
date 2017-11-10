# object for tracking game status
import random

# dictionaries
FILE_ROOT="/Users/jporter/code/codenames"
DICTIONARIES={
    "CAH" :         FILE_ROOT + "/cah_code_names.txt", 
    "Pop Culture" : FILE_ROOT + "/code_names_pop.txt", 
    "Dictionary" :  FILE_ROOT + "/code_names_dict.txt", 
    "Simple" :      FILE_ROOT + "/code_names_simple.txt"
}
# colors per team
RED = 'R'
BLUE = 'B'
GREEN = 'G'
# num words per board
NUM_WORDS_NORMAL=25
NUM_WORDS_BIG=81
BIG_BLACKOUT_SPOTS=[4,20,24,36,40,44,56,60,76]

class Info:
    def __init__(self, dictionary='Dictionary', seed=None, size=NUM_WORDS_NORMAL, players=2):
        self.adv_color = 'adv_color' #what is this
        self.dictionary = dictionary
        self.players = players
        self.size = size
        self.layout = self.__get_layout()
        self.words = self.__get_words()
        self.solution = dict(zip(self.words, self.layout))


    def __get_words(self):
        if not self.dictionary in DICTIONARIES.keys():
            print ("Error: dictionary '" + self.dictionary + "' doesn't exist")
            return None
        words_file = open(DICTIONARIES[self.dictionary], 'r')
        words = [elem for elem in words_file.read().split('\n') if len(elem.strip()) > 0]
        random.shuffle(words)
        final_words = words[0:self.size]
        return final_words

    def __get_layout(self):
        self.adv_color = RED
        green = 0
        if self.size == NUM_WORDS_NORMAL:
            if self.players==3:
                blue = 5
                red = 5
                green = 5
            else:
                blue = 8
                red = 8

            bystanders = 25 - blue - red - green - 2
        else:
            if self.players == 2:
                blue = 8
                red = 8
            elif self.players == 3:
                blue = 8
                red = 8
                green = 8
            num_blackouts = 9
            bystanders = 81 - num_blackouts - blue - red - green - 3
        if self.players == 2:
            if random.random() < 0.5:
                blue += 1
                self.adv_color = BLUE
            else:
                red += 1
        else:
            if random.random() < 0.333:
                blue += 1
                self.adv_color = BLUE
            elif random.random() > 0.666:
                green += 1
                self.adv_color = GREEN
            else:
                red += 1
        mix = ["B"] * blue
        mix.extend(["R"] * red)
        if green > 0:
            mix.extend(['G'] * green)
        mix.extend(["X"])
        if self.size == NUM_WORDS_BIG:
            mix.extend(['X'])
        mix.extend(["O"] * bystanders)
        random.shuffle(mix)
        if self.size == NUM_WORDS_BIG:
            for i in BIG_BLACKOUT_SPOTS:
                mix.insert(i, '-')
        return mix

