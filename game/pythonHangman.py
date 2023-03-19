from game.data.database import Database
import random

class Display:
    def __init__(self):
        self.maxGuesses = 7
        self.missedLetters = 0
        self.incorrectGuesses = 1
        self.database = Database()
        self.phrase = self.get_puzzle()
        self.lettersGuessed = []
        

    #Function that houses the progress of the program by controlling loops
    #for gameplay and checks for game completion
    def control(self, gamertag):
        display1 = Display()
        # While the player hasn't missed too many guesses or completed the puzzle.
        # they will be able to keep guessing
        while (display1.incorrectGuesses < display1.maxGuesses):
            reader = input("Please guess a letter:")
            # Set 'x' as an input value for the game control
            x = reader
            x = x.lower()
            print()
            # If/Elif is used to determine if the guess is part of the phrase or not.
            # Returns a count of missed letters to Display.missedLetters variable
            if x in display1.phrase.lower():
                display1.missedLetters = display1.correctGuess(display1, x)
            elif x not in display1.phrase.lower():
                display1.missedLetters = display1.incorrectGuess(display1, x)

            # If the player guessed all the letters, they win.
            # Otherwise, if they miss too many guesses they lose.
            if (display1.missedLetters == 0):
                display1.incorrectGuesses = display1.maxGuesses
                self.database.change_puzzles(gamertag, self.phrase)
                print("You got all of the letters! You won!")
                print()
            elif (display1.incorrectGuesses == display1.maxGuesses):
                print("You hung the man. You lost at hang man. He's dead. Sorry.")
                print()

    #Function to create the display of data for gameplay.
    #It shows a display of the hangman graphic, guessed letters,
    #number of missed guesses left, and determines missed guesses.
    def createDisplay(self, display):
        counter = 0
        displayArray = ["  |  ", "  () ", "  -  ", " /|\\ ", " --- ", " || ", " __ "]
        # Loop to display the status of the hangman graphic.
        for i in range(1, display.incorrectGuesses):
            print(displayArray[i-1])
        print()
        # Loop to display the guessed and missed letters of the puzzle.
        for i in range(1,len(display.phrase)+1):
            letter = display.phrase[i-1]
            if (letter.lower() in display.lettersGuessed):
                print(letter, end =" ")
            elif ( letter == " "):
                print(" ", end =" ")
            else:
                counter += 1
                print("_", end =" ")

        #If the player guesses all the letters then println()
        #Otherwise, update Document.missedLetters count.
        if (counter == 0):
            print()
        else:
            print()
            display.missedLetters = counter

        # Display guessed letters and number of missed guesses left.
        print("Letters you've guessed already:", end =" ")
        for i in range(1, len(display.lettersGuessed) + 1):
            print(display.lettersGuessed[i-1], end =" ")
        print()
        print(f'You have {display.maxGuesses-display.incorrectGuesses} missed guesses left.')
        return counter

    # Function to handle a correct guess from the player.
    # It returns a number of missed letters upon completion.
    def correctGuess(self, display, guess):
        if (guess.lower() in display.lettersGuessed):
            print("That's a correct guess, but you already guessed it. Try a different letter")
        else:
            display.lettersGuessed.append(guess.lower())
        return self.createDisplay(display)

    # Function to handle an incorrect guess from the player.
    # It returns a number of missed letters upon completion.
    def incorrectGuess(self, display, guess):
        if (guess in display.lettersGuessed):
            print("That's an incorrect guess and you already guessed it. Try a different letter")
        else:
            display.lettersGuessed.append(guess.lower())
            display.incorrectGuesses += 1
        return self.createDisplay(display)
    
    # Function to retrieve a random puzzle from the Firebase database
    def get_puzzle(self):
        docs = self.database.get_data('puzzles')
        num = int(random.randrange(1,5))
        for doc in docs:
            if int(doc.id) == num:
                dictionary = doc.to_dict()
                puzzle = dictionary['puzzle']
                return puzzle
    # Function to check if gamertag is already created
    def is_user(self, gamertag):
        docs = self.database.get_data('users')
        for doc in docs:
            dictionary = doc.to_dict()
            gt = dictionary['gamertag']
            if gt == gamertag:
                return True
        return False
    
    # Function to give user options to change or delete gamertag
    def menu(self, gamertag):
        option = 0
        while (option !=3):
            option = int(input("""
Push '1' to Change Gamertag 
Push '2' to Delete Gamertag
Push '3' to Play
"""))
            if option == 1:
                newtag = input('What would you like your new gamertag to be? ')
                self.database.change_gamertag(gamertag, newtag)
            elif option == 2:
                self.database.delete_data(gamertag)
                newtag = input('What would you like your new gamertag to be? ')
                self.database.add_data('users', newtag)

    # Function to start the program and house control function.
    def main(self):
        print("Welcome to Hangman!")
        print("")
        print("Phrases are generated automatically.")
        print("")
        gamertag = input('Please enter your gamertag: ')
        if not self.is_user(gamertag):
            self.database.add_data('users', gamertag)
        self.menu(gamertag)
        self.control(gamertag)
