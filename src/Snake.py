# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Rabbit class



from Creature import Creature

class Snake(Creature):
    def __init__(self, row, col):
        """
        Initialize a snake object
        :param row: row coordinate
        :param col: col coordinate
        """
        Creature.__init__(self, "S", row, col)
