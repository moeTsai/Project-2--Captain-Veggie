# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Veggie class

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):

    def __init__(self, name, symbol, points):
        """
        Initializes a new instance of the Veggie class.

        :param name: The name of the Veggie.
        :param symbol: The symbol of the Veggie.
        :param points: The points associated with the Veggie.
        """
        
        super().__init__(symbol)
        self.__name = name
        self.__points = points

    def __str__(self):
        """
        Returns a string representation of the Veggie.

        :return: The string representation of the Veggie.
        """
        return f"Symbol: {self.symbol}, Name: {self.__name}, Points: {self.__points}"

    def getName(self):
        """
        Gets the name of the Veggie.

        :return: The name of the Veggie.
        """
        return self.__name

    def setName(self, name):
        """
        Sets the name of the Veggie.

        :param name: The new name of the Veggie.
        """
        self.__name = name

    def getPoints(self):
        """
        Gets the points associated with the Veggie.

        :return: The points associated with the Veggie.
        """
        return self.__points

    def setPoints(self, points):
        """
        Sets the points associated with the Veggie.

        :param points: The new points associated with the Veggie.
        """
        self.__points = points
