# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: creature class


from FieldInhabitant import FieldInhabitant

class Creature:
    def __init__(self, symbol,x,y):
        FieldInhabitant.__init__(self,symbol)
        self._x = x
        self._y = y


    def setX(self,x):
        """
        setter for coordinate x
        :param x: new coordinate x
        :return: none
        """
        self._x = x

    def getX(self):
        """
        getter for coordinate x
        :return: coordinate x
        """
        return self._x

    def setY(self,y):
        """
        setter for coordinate y
        :param y: new coordinate y
        :return: none
        """
        self._y =y

    def getY(self):
        """
        getter for coordinate y
        :return: coordinate y
        """
        return self._y