# PWC - a Python Wordle Clone
# Plays just like the real thing if it was played using the command line.
# Word list comes from the "Sunshine" English textbooks.
# Letters in the correct spot are shown using uppercase letters.
# Letters that are in the word but in the wrong spot are shown using lowercase letters.
# Letters that are not in the word are shown using an underscore (_)
# Enjoy! :]

import random

wordSolved = False

def compare(t, g, guessProgress):
    """
    Compare the guess with the target word, letter-by-letter.
    If the letter is in the correct place, use a capital letter.
    If the letter is correct but in the wrong place, use a lowercase letter.
    Update progress
    """
    for i in range(5):
        if t[i] == g[i]:
            guessProgress[i] = t[i].upper()
        elif g[i] in t:
            guessProgress[i] = g[i].lower()
        else:    
            guessProgress[i] = '_'

#begin the game by importing the vocabulary and selecting a word
def initialise:
    wordList = ['apple', 'break', 'catch', 'dance', 'enter', 'fruit']
    targetWord = list(wordList[random.randint(0,len(vocab))])
    progress = ['_'] * 5
    wordSolved = False
    return targetWord

#get input
#check if any letters are in the same position
#reprint word with matches
while wordSolved == False:
        guess = input("please guess a 5-letter word:\n")
        guessList = list(guess)
        compare(targetWord, guessList, progress)
        print(progress)
        
    ////////////////////////////////////////////////////////////////////
# A Python Wordle clone

import random

class Game:
    def __init__(self):
        self.dictionary = ['apple', 'break', 'catch', 'dance', 'enter', 'fruit', 'grape']
        self.gameOver = False
        self.remainingTurns = 6
        self.targetWord = None
        return None

    # Compare the guess with the target word.
    def compareGuess(t, g, guessProgress):
        for i in range(5):
            if t[i] == g[i]:
                guessProgress[i] = t[i].upper()
            elif g[i] in t:
                guessProgress[i] = g[i].lower()
            else:    
                guessProgress[i] = '_'

    #begin the game by importing the vocabulary and selecting a word
    def start():
        targetWord = list(wordList[random.randint(0, 5)])
        progress = ['_'] * 5
        wordSolved = False
        return targetWord

NewGame = Game()
NewGame.start()
while NewGame.gameOver == False:
    playerGuess = input("please guess a 5-letter word:\n")
        guessList = list(guess)
        compare(targetWord, guessList, progress)
        print(progress)
        
    
    
    
    
    
    
        
    
    
    
    
    
