# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Captain class


from Creature import Creature


class Captain(Creature):
    def __init__(self,symbol,x,y):
        Creature.__init__(self,"V",x,y)
        self.__veggieList = []


    def addVeggie(self,veggie):
        self.__veggieList.append(veggie)

    def getVeggieList(self):
        return self.__veggieList