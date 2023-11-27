# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Rabbit class



from Creature import Creature

class Rabbit(Creature):
    def __init__(self, symbol, x, y):
        """
        Initialize a rabbit object
        :param symbol: symbol of rabbit object
        :param x: x coordinate
        :param y: y coordinate
        """
        Creature.__init__(self, "R", x, y)