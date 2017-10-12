BLUE = 'B'
RED = 'R'
GREEN = 'G'

class GameInfo:
    def __init__(self, game_id=0, adv_color='', layout='', words=[]):
        self.game_id = game_id
        self.adv_color = adv_color
        self.layout = layout
        self.words = words

