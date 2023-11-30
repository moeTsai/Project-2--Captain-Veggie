# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: creature class


from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self,symbol, row, col):
        FieldInhabitant.__init__(self,symbol)
        self.__row = row
        self.__col = col


    def setRow(self,row):
        """
        setter for row coordinate
        :param row: new row coordinate
        :return: none
        """
        self.__row = row

    def getRow(self):
        """
        getter for row coordinate
        :return: row coordinate
        """
        return self.__row

    def setCol(self,col):
        """
        setter for col coordinate
        :param col: new col coordinate
        :return: none
        """
        self.__col = col

    def getCol(self):
        """
        getter for col coordinate
        :return: col coordinate
        """
        return self.__col