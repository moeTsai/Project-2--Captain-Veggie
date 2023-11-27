# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Captain class


from Creature import Creature


class Captain(Creature):
    def __init__(self,symbol,x,y):
        """
        initialize a new instance of Captain object
        :param symbol: Symbol of Captain
        :param x: x coordinate
        :param y: y coordinate
        """
        Creature.__init__(self,"V",x,y)
        self.__veggieList = []


    def addVeggie(self,veggie):
        """
        add veggie into veggieList
        :param veggie: veggie object
        :return: none
        """
        self.__veggieList.append(veggie)

    def getVeggieList(self):
        """
        function get the veggieList
        :return: veggieList
        """
        return self.__veggieList