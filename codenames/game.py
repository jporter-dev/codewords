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


class Info:
    def __init__(self, dictionary='Dictionary', seed=None, size=NUM_WORDS_NORMAL):
        self.adv_color = 'adv_color' #what is this
        self.dictionary = dictionary
        self.size = size
        self.layout = self.__get_layout()
        self.words = self.__get_words()

    def __get_words(self):
        if not self.dictionary in DICTIONARIES.keys():
            print ("Error: dictionary '" + dictionary + "' doesn't exist")
            return None
        words_file = open(DICTIONARIES[self.dictionary], 'r')
        words = [elem for elem in words_file.read().split('\n') if len(elem.strip()) > 0]
        random.shuffle(words)
        final_words = words[0:self.size]
        return final_words

    def __get_layout(self):
        print('asdf')

