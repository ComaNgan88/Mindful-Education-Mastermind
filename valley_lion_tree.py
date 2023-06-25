# Code for "Mastermind Group for Educators" in Python

# Imports libraries and packages
import random
import itertools

# Defines the function to generate the game board
def createGameBoard():
    board = []
    # Makes a list of all possible colors
    colors = ["red", "blue", "yellow", "green"]

    # Iterate 4 times to generate the game board
    for i in range(4):
        # Add a randomly selected color to the board
        board.append(random.choice(colors))
    return board

# Defines the function to check the user's input
def checkUserInput(userInput, board):
    # Makes a list to hold the results
    results = []
    # Iterate through each input
    for i in range(len(board)):
        # Check if the colors are correct and in the correct order
        if userInput[i] == board[i]:
            results.append("correct")
        # Check if the colors are correct but in the incorrect order
        elif userInput[i] in board:
            results.append("misplaced")        
        # Check if the colors are incorrect
        else:
            results.append("wrong")
    # Returns the results
    return results

# Defines the function to check for a win
def checkForWin(userInput, board):
    # Makes a list to hold the results
    results = []
    # Iterate through each input
    for i in range(len(board)):
        # Check if the colors are correct and in the correct order
        if userInput[i] == board[i]:
            results.append("correct")
    # Check if all 4 results are correct
    if len(results) == 4:
        return True
    else:
        return False

# Defines the main function
def main():
    # Generates the game board
    board = createGameBoard()
    # Sets the number of guesses to 0
    numGuesses = 0

    # Prints welcome message
    print("Welcome to Mastermind!")
    # Prints the rules of the game
    print("\nThe rules are as follows: You have twelve guesses to guess the four colors. You will be shown the result of each guess and the number of guesses you have made.")
    # Prints the colors
    print("\nColors: red, blue, yellow, green")

    # Loops until the user has made 12 guesses or won the game
    while numGuesses < 12:
        # Gets user input
        userInput = input("\nPlease enter your guess: ").split()
        # Tells the user the number of guesses they have made
        print("\nYou have made " + str(numGuesses) + " guesses.")
        # Increments number of guesses
        numGuesses += 1
        # Checks the user's input
        results = checkUserInput(userInput, board)
        # Prints the results
        print("\nResults: " + str(results))
        # Checks if the user won
        if checkForWin(userInput, board):
            # Prints winning message
            print("\nCongratulations! You have won!")
            # Breaks out of the loop
            break
        # Checks if the user has made 12 guesses
        elif numGuesses == 12:
            # Prints game over message
            print("\nGame Over. You have made 12 guesses and have not won.")    

# Runs the main function
main()