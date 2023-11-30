# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Rabbit class



from Creature import Creature

class Rabbit(Creature):
    def __init__(self, row, col):
        """
        Initialize a rabbit object
        :param row: row coordinate
        :param col: col coordinate
        """
        Creature.__init__(self, "R", row, col)

    # def setRow(self, row):
    #     """
    #     Set row coordinate
    #     :param row: row coordinate
    #     :return: none
    #     """
    #     self.__row = row

    # def setCol(self, col):
    #     """
    #     Set col coordinate
    #     :param col: col coordinate
    #     :return: none
    #     """
    #     self.__col = col

    # def getRow(self):
    #     """
    #     Get row coordinate
    #     :return: row coordinate
    #     """
    #     return self.__row
    
    # def getCol(self):
    #     """
    #     Get col coordinate
    #     :return: col coordinate
    #     """
    #     return self.__col