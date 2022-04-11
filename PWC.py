# PWC - a Python Wordle Clone
# Plays just like the real thing if it was played using the command line.
# Word list comes from the "Sunshine" English textbooks.
# Letters in the correct spot are shown using uppercase letters.
# Letters that are in the word but in the wrong spot are shown using lowercase letters.
# Letters that are not in the word are shown using an underscore (_)
# Enjoy! :]
import random

class Game:
    def __init__(self):
        self.dictionary = ['apple', 'break', 'catch', 'dance', 'enter', 'fruit', 'grape']
        self.wordSolved = False
        self.gameOver = False
        self.remainingTurns = 6
        self.targetWord = None
        return None

    def compareGuess(self,g):     #Compare the guess with the target word.
        t = list(self.targetWord)
        guessProgress = ['_'] * 5
        for i in range(5):
            if t[i] == g[i]:
                guessProgress[i] = t[i].upper()
            elif g[i] in t:
                guessProgress[i] = g[i].lower()
            else:    
                guessProgress[i] = '_'
        print(guessProgress)

    def start(self): #Begin the game by selecting a word.
        self.targetWord = list(self.dictionary[random.randint(0, 5)])
        self.wordSolved = False
        print(self.targetWord)

NewGame = Game()
NewGame.start()
while NewGame.gameOver == False:
    while True:
        playerGuess = input("Please guess a 5-letter word:\n")
    #validate user input
    #check that the guess is 5 letters long
        if len(playerGuess) != 5:
            print("Sorry, please make sure the word is 5 letters only.")
            continue
        else:
            break
    #check that there are no numbers
    #check that there are no special characters
    #(later)check that the input is a real word
    #convert guess to lower case
    guessList = list(playerGuess)
    NewGame.compareGuess(guessList)
    
