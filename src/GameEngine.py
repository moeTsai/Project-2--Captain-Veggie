# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: GameEngine class


class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = 'highscore.data'
    
    def __init__(self):
        """
        Initializes a new instance of the GameEngine class.
        
        :return: A new instance of the GameEngine class.
        """
        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__vegetables = []
        self.__score = 0

    
    def initVeggies():
        pass

    def initCaptain():
        pass

    def initRabbits():
        pass

    def initializeGame():
        pass

    def remainingVeggies():
        pass

    def intro():
        pass

    def printField():
        pass

    def getScore():
        pass


    def getVeggiesNum(cls):
        """
        Return the number of veggies in the game
        
        :return: number of veggies
        """
        return cls.__NUMBEROFVEGGIES

    def getNumberOfRabbits(cls):
        """
        Return the number of rabbits in the game
        
        :return: number of rabbits
        """
        return cls.__NUMBEROFRABBITS


    def getHighScoreFile(cls):
        """
        Return the high score file name
        
        :return: high score file name
        """
        return cls.__HIGHSCOREFILE


    def getField(self):
        """
        Return the field
        
        :return: field
        """
        return self.__field

    def setField(self, field):
        """
        Set the field

        :param field: field
        """
        self.__field = field

    def getRabbits(self):
        """
        Return the rabbits
        
        :return: rabbits
        """
        return self.__rabbits

    def setRabbits(self, rabbits):
        """
        Set the rabbits
        
        :param rabbits: rabbits
        """
        self.__rabbits = rabbits

    def getCaptain(self):
        """
        Return the captain
        
        :return: captain
        """
        return self.__captain

    def setCaptain(self, captain):
        """
        Set the captain
        
        :param captain: captain
        """
        self.__captain = captain


    def getVegetables(self):
        """
        Return the vegetables
        
        :return: vegetables
        """
        return self.__vegetables


    def setVegetables(self, vegetables):
        """
        Set the vegetables
        
        :param vegetables: vegetables
        """
        self.__vegetables = vegetables


    def getScore(self):
        """
        Return the score
        
        :return: score
        """
        return self.__score

    def setScore(self, score):
        """
        Set the score
        
        :param score: score
        """
        self.__score = score