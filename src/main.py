# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: Main function of the program

from GameEngine import GameEngine


"""
In a file named main.py, you should have:
o Your main function in which:
▪ You instantiate and store a GameEngine object
▪ Initialize the game using the appropriate GameEngine function
▪ Display the game’s introduction using the appropriate GameEngine function
▪ Create an variable to store the number of remaining vegetables in the game, initialized
using the appropriate GameEngine function
▪ While there are still vegetables left in the game
• Output the number of remaining vegetables and the player’s score
• Print out the field using the appropriate GameEngine function
• Move the rabbits using the appropriate GameEngine function
• Move the captain using the appropriate GameEngine function
• Determine the new number of remaining vegetables using the appropriate
GameEngine function
▪ Display the Game Over information using the appropriate GameEngine function
▪ Handle the High Score functionality using the appropriate GameEngine function
"""




def main():
    """
    Main function of the program
    """
    game = GameEngine()
    game.initializeGame()

    game.intro()
    numVeggies = game.remainingVeggies()
    while numVeggies > 0:
        print(str(numVeggies) + " veggies remaining. Current score: " + str(game.getScore()))
        game.printField()
        game.moveRabbits()
        game.moveCaptain()
        numVeggies = game.remainingVeggies()
        
    game.gameOver()
    game.highScore()

if __name__ == "__main__":
    main()