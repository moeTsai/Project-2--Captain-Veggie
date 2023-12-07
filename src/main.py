# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Main function of the program

from GameEngine import GameEngine






def main():
    """
    Main function of the program
    """

    # Initialize the game
    game = GameEngine()
    game.initializeGame()
    # Start the game
    game.intro()
    numVeggies = game.remainingVeggies()
    while numVeggies > 0:
        print(str(numVeggies) + " veggies remaining. Current score: " + str(game.getScore()))
        game.printField()
        game.moveRabbits()
        game.moveCaptain()
        numVeggies = game.remainingVeggies()
    
    # End the game
    game.gameOver()
    game.highScore()

if __name__ == "__main__":
    main()