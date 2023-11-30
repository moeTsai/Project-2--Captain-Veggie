# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: GameEngine class

import os.path
import random
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit

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

        self.__veggieWorth = {}
        self.__veggieSymbol = {}




    def randomLocation(self, row, col):
        """
        Return a random location in the field
        
        :param row: row number
        :param col: column number
        :return: a random location in the field
        """
        randomRow = random.randint(0, row - 1)
        randomCol = random.randint(0, col - 1)
        return randomRow, randomCol

    
    def initVeggies(self):
        """
        Initialize the field and veggies
        """
        # The user is prompted for the name of the veggie file, and if the user’s file name doesn’t
        file = input("Please enter the name of the vegetable point file: ")

        # prompt the user until they enter a valid file name
        while not os.path.exists(file):
            file = input(f"{file} does not exist! Please enter the name of the vegetable point file: ")

        with open(file, 'r') as f:
            row = 0
            col = 0
            for line in f:
                line = line.strip()
                line = line.split(",")
                # read the field size
                if line[0] == "Field Size":
                    row = int(line[1])
                    col = int(line[2])
                    self.__field = [[None for i in range(col)] for j in range(row)]
                    continue

                # read the veggie name, symbol, and point
                self.__veggieSymbol[line[0]] = line[1]
                self.__veggieWorth[line[1]] = int(line[2])
        possibleVeggies = list(self.__veggieSymbol.keys())

        for _ in range(self.__NUMBEROFVEGGIES):
            randomRow, randomCol = self.randomLocation(row, col)
            while self.__field[randomRow][randomCol]:
                randomRow, randomCol = self.randomLocation(row, col)
            
            generatedVeggie = random.choice(possibleVeggies)
            symbol = self.__veggieSymbol[generatedVeggie]
            point = self.__veggieWorth[symbol]
            veggie = Veggie(generatedVeggie, symbol, point)

            self.__field[randomRow][randomCol] = veggie
            self.__vegetables.append(veggie)
        
        

        

    def initCaptain(self):
        row = len(self.__field)
        col = len(self.__field[0])
        randomRow, randomCol = self.randomLocation(row, col)
        while self.__field[randomRow][randomCol]:
            randomRow, randomCol = self.randomLocation(row, col)
        self.__captain = Captain(randomRow, randomCol)
        self.__field[randomRow][randomCol] = self.__captain
        

    def initRabbits(self):
        row = len(self.__field)
        col = len(self.__field[0])
        for _ in range(self.__NUMBEROFRABBITS):
            randomRow, randomCol = self.randomLocation(row, col)
            while self.__field[randomRow][randomCol]:
                randomRow, randomCol = self.randomLocation(row, col)
            rabbit = Rabbit(randomRow, randomCol)
            self.__rabbits.append(rabbit)
            self.__field[randomRow][randomCol] = rabbit


    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        return len(self.__vegetables)

    def intro(self):
        pass



    def printField(self):
        """
        The contents of the field are output in a pleasing 2D grid format with a border around the entire grid
        """
        # print border########################################
        for _ in range(len(self.__field[0]) * 2 + 2):
            print("#", end="")
        print()
        
        for i in range(len(self.__field)):
            print("#", end="")
            for j in range(len(self.__field[0])):
                if self.__field[i][j]:
                    print(self.__field[i][j].getSymbol(), end=" ")
                else:
                    print(" ", end=" ")
            print("#")

        for _ in range(len(self.__field[0]) * 2 + 2):
            print("#", end="")
        pass

    def getScore(self):
        return self.__score
        pass

    def removeVeggie(self, row, col):
        """
        Remove the veggie at the given location
        
        :param row: row number
        :param col: column number
        """
        self.__vegetables.remove(self.__field[row][col])
        self.__field[row][col] = None
        
        pass

    def moveRabbits(self):
        """
         the rabbit could move 1 space up, down, left, right, any diagonal direction,
        or possibly not move at all
        • If a Rabbit object attempts to move outside the boundaries of field it will
        forfeit its move
        • If a Rabbit object attempts to move into a space occupied by another Rabbit
        object or a Captain object it will forfeit its move
        • If a Rabbit object moves into a space occupied by a Veggie object, that
        Veggie object is removed from field, and the Rabbit object will take its
        place in field
        • Note that Rabbit object’s appropriate member variables should be updated
        with the new location as well
        • Make sure you set the Rabbit object’s previous location in the field to None if
        it has moved to a new location
        """
        direction = [[-1, -1], [-1, 0], [-1, 1], 
                     [0, -1], [0, 0], [0, 1],
                       [1, -1], [1, 0], [1, 1]]
        for rabbit in self.__rabbits:
            randomDirection = random.randint(0, 8)
            attemptRow = rabbit.getRow() + direction[randomDirection][0]
            attemptCol = rabbit.getCol() + direction[randomDirection][1]
            if (attemptRow < 0 or attemptRow >= len(self.__field)
                 or attemptCol < 0 or attemptCol >= len(self.__field[0])):
                continue
            
            
            # if the rabbit is moving to a space occupied by another rabbit or captain, forfeit its move
            if (self.__field[attemptRow][attemptCol] and
                self.__field[attemptRow][attemptCol].getSymbol() in ["R", "V"]):
                continue

            # if the rabbit is moving to a space occupied by veggie, remove the veggie
            if (self.__field[attemptRow][attemptCol] and 
                self.__field[attemptRow][attemptCol].getSymbol() in list(self.__veggieSymbol.values())):
                self.removeVeggie(attemptRow, attemptCol)

            self.__field[attemptRow][attemptCol] = rabbit
            self.__field[rabbit.getRow()][rabbit.getCol()] = None
            rabbit.setRow(attemptRow)
            rabbit.setCol(attemptCol)


        pass

    def moveC(self, row, col):
        """
        Move the captain to the given location

        :param row: row number
        :param col: column number
        """
        self.__field[self.__captain.getRow()][self.__captain.getCol()] = None
        self.__captain.setRow(row)
        self.__captain.setCol(col)
        self.__field[row][col] = self.__captain
        
        pass




    def moveCptVertical(self, direction):
        newCptRow = self.__captain.getRow() + direction
        newCptCol = self.__captain.getCol()

        # If the Captain object’s current position plus the movement
        #  would move them into an empty slot in field
        if not self.__field[newCptRow][newCptCol]:
            self.moveC(newCptRow, newCptCol)
            return
        
        # if the Captain object’s current position plus the movement would move
        # them into a space occupied by a Veggie object
        if self.__field[newCptRow][newCptCol].getSymbol() in list(self.__veggieSymbol.values()):
            point = self.__veggieWorth[self.__field[newCptRow][newCptCol].getSymbol()]
            self.__score += point
            self.__captain.addVeggie(self.__field[newCptRow][newCptCol])
            # print out the message
            print(f"Yummy! A delicious {self.__field[newCptRow][newCptCol].getName()}!")
            self.removeVeggie(newCptRow, newCptCol)

            self.moveC(newCptRow, newCptCol)
            return

        # Inform the player that they should not step on the rabbits, do not move the Captain object
        if self.__field[newCptRow][newCptCol].getSymbol() == "R":
            print("Don't step on the bunnies!")
            return
        

        


        pass

    def moveCptHorizontal(self, direction):
        # same as moveCptVertical
        newCptRow = self.__captain.getRow()
        newCptCol = self.__captain.getCol() + direction

        # If the Captain object’s current position plus the movement
        #  would move them into an empty slot in field
        if not self.__field[newCptRow][newCptCol]:
            self.moveC(newCptRow, newCptCol)
            return
        
        # if the Captain object’s current position plus the movement would move
        # them into a space occupied by a Veggie object
        if self.__field[newCptRow][newCptCol].getSymbol() in list(self.__veggieSymbol.values()):
            point = self.__veggieWorth[self.__field[newCptRow][newCptCol].getSymbol()]
            self.__score += point
            self.__captain.addVeggie(self.__field[newCptRow][newCptCol])
            # print out the message
            print(f"Yummy! A delicious {self.__field[newCptRow][newCptCol].getName()}!")
            self.removeVeggie(newCptRow, newCptCol)

            self.moveC(newCptRow, newCptCol)
            return

        # Inform the player that they should not step on the rabbits, do not move the Captain object
        if self.__field[newCptRow][newCptCol].getSymbol() == "R":
            print("Don't step on the bunnies!")
            return

        pass

    def moveCaptain(self):
        """
        captian movement
        """
        # The player is prompted for the direction they would like to move the Captain object
        keyPress = input("\nWould you like to move up(W), down(S), left(A), or right(D): ")

        # accept both upper and lower case
        keyPress = keyPress.upper()

        # The player’s input is validated to ensure it is one of the four valid options
        if keyPress not in ["W", "S", "A", "D"]:
            print(f"{keyPress} is not a valid option")
            return

        # movement conditions
        if keyPress == "W" and self.__captain.getRow() > 0:
            self.moveCptVertical(-1)
        elif keyPress == "S" and self.__captain.getRow() < len(self.__field) - 1:
            self.moveCptVertical(1)
        elif keyPress == "A" and self.__captain.getCol() > 0:
            self.moveCptHorizontal(-1)
        elif keyPress == "D" and self.__captain.getCol() < len(self.__field[0]) - 1:
            self.moveCptHorizontal(1)
        else:
            print("You can't move that way!")


        pass

    def gameOver(self):
        """
        ▪ The player is informed the game is over
        ▪ The names of all of the vegetables the Captain object harvested are output
        ▪ The player’s score is output
        """


        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for veggie in self.__captain.getVeggieList():
            print(veggie.getName())
        print(f"Your score was: {self.__score}")
        
        pass

    def highScore(self):
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

    def appendVeggieWorth(self, veggie, worth):
        """
        Append the veggie worth
        
        :param veggie: veggie
        :param worth: worth
        """
        self.__veggieWorth[veggie] = worth

    def getVeggieWorth(self):
        """
        Return the veggie worth
        
        :return: veggie worth
        """
        return self.__veggieWorth