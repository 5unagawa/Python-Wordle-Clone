# PWC - a Python Wordle Clone
# Plays just like the real thing if it was played using the command line.
# Word list comes from the "Sunshine" English textbooks.
# Letters in the correct spot are shown using uppercase letters.
# Letters that are in the word but in the wrong spot are shown using lowercase letters.
# Letters that are not in the word are shown using an underscore (_)
# Enjoy! :]
from vocablist import dictionary
import random

class Game:
    def __init__(self):
        self.gameDictionary = dictionary
        self.wordSolved = None
        self.gameOver = False
        self.remainingTurns = None
        self.targetWord = None
        return None
    
    def checkGuess(self,g):     #Compare the guess with the target word. Returns True if the word is a match.
        t = list(self.targetWord)
        guessProgress = ['_'] * 5
        for i in range(5):
            if g[i] == t[i]:
                guessProgress[i] = t[i].upper()
            elif g[i] in t:
                guessProgress[i] = g[i].lower()
            else:    
                guessProgress[i] = '_'
        print(guessProgress)
        if guessProgress == t:
            return True
        else:
            return False
    
    def gameSetup(self): #Begin the game by selecting a word.
        self.targetWord = random.choice(self.gameDictionary).upper() 
        self.wordSolved = False
        self.remainingTurns = 6
        
    def gameLoop(self):
        self.gameSetup()
        print("Welcome to PWC - a Python Wordle Clone\n"
            +"Plays just like the real thing if it was played using the command line.\n"
            +"Letters in the correct spot are shown using uppercase letters.\n"
            +"Letters that are in the word but in the wrong spot are shown using lowercase letters.\n"
            +"Letters that are not in the word are shown using an underscore (_)\n"
            +"Enjoy! :]")
        while not (NewGame.remainingTurns == 0 or NewGame.wordSolved == True):
            while True:
                playerGuess = input("Please guess a 5-letter word:\n")
                #validate user input
                #check that the guess is 5 letters long
                if len(playerGuess) != 5:
                    print("Sorry, please make sure the word is 5 letters only.")
                    continue
                #check that the guess is letters only
                elif playerGuess.isalpha() == False:
                    print("Sorry, you can only use letters.")
                else:
                    break
                #(later)check that the input is a real word
            #convert guess to lower case and into array
            guessList = list(playerGuess.upper())
            NewGame.wordSolved = NewGame.checkGuess(guessList)
            NewGame.remainingTurns -= 1
            print("You have " + str(NewGame.remainingTurns) + " turns left.")
        if NewGame.wordSolved == True:
            print("Well done!")
        else:
            print("You ran out of guesses. The word was: " + NewGame.targetWord)
        
        while True:
            replay = input("Would you like to play again? Y/N").upper()
            if replay == "Y":
                break
            elif replay == "N":
                NewGame.gameOver = True
                break
            else:
                print("Please enter Y or N")
                continue
            
NewGame = Game()
while NewGame.gameOver == False:
    NewGame.gameLoop()
print("Game over. Thank you so much for to playing my game.")
