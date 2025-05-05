# Name: Your name or you and your partner's name
# Date: 
# Per#:
# Title: word_guess.py
# pseudocode: Create a word game where the player has
# twelve chances to guess the word by selecting letters.

# import libraries
import random
import os

# clear the standard output screen
os.system("clear")

name = input("What is your name?: ")
print(f"Good Luck {name}!")

# computer science word list
words = ['computer', 'hardware', 'software', 'operating system', 
         'prgramming language', 'python', 'linux', 'program', 'mouse',
         'power supply', 'hdmi cable', 'monitor', 'keyboard',
         'screen', 'standard output', 'raspberry pi', 

         'mathematics', 'addition', 'subtraction', 'multiplication',
         'division', 'sum', 'difference', 'product', 'quotient',
         'exponent', 'exponentiation',

         'editor', 'nano', 'file name', 'directory', 

         'variable', 'variable types', 'boolean', 'float', 'integer', 
         'string', 'f-string', 'floating point', 'character string',
         'list', 'true', 'false', 'binary', 'append',

         'comment', 'define', 'argument', 'parameter', 'index'
         'statement', 'function call', 'condition', 'rgb'

         'function', 'print', 'input', 'print statement', 'input statement',  
         'loops', 'for loop', 'for', 'range', 'enumerate', 
         'while loop', 'while', 'flag', 'set flag', 'check flag', 'reset flag',  
         'conditional statements', 'conditional', 'if', 'elif', 'else', 

         'library', 'random', 'time',
        
         'parenthesis', 'single quotes', 'double quotes', 'colon',
         'dunder', 'hashtag', 'number sign', 'curly braces',
         'square brackets', 'underscore', 'less than', 'greater than',
         'indentation', 'tab', 'spaces',  

         'commands', 'ls', 'cd', 'cat', 'python3', 'alt shift 3', 'control x', 
         'enter', 'cut', 'paste', 'control k', 'control u', 'remove', 'move',
         'touch', 'make directory', 'remove directory', 'concatenate', 'run',
         'execute', 'save'
        ]

word = random.choice(words)

print("Guess the characters")
guesses = ' -'
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end="")

        else:
            print("_", end="")
            failed = failed + 1

    if failed == 0:
        print("")
        print(f"You Win {name}!")
        print(f"The word(s) is: {word}")
        break

    print()
    print(f"Tried: {guesses}")

    # validate input
    while True:
        guess = input(f"Guess a character: ")
        if len(guess) > 1:
            print("Invalid Input")
        else:
            guesses = guesses + guess
            break

    if guess not in word:

        turns = turns - 1
        print("Wrong")
        print(f"You have {turns} more guesses")

        if turns == 0:
            print("You Loose.")
            print(f"The word(s) is {word}.")
