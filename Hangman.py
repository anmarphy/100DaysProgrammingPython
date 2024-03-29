import string
import random
from replit import clear
from python_words import words
from hangmang_resources import hangmanpics

alphabet = list(string.ascii_lowercase)
print(f'Total lives: {len(hangmanpics)}')
lives=len(hangmanpics)


# step 1: Selecting the word
word=random.choice(words)
print(f'You have a total of {lives} to guess {word.upper()}')

# step 2: Generating the blanks
blank=[]
for i in range(len(word)):
   blank.append('_')

continue_game=True

while continue_game:
    # step 3: Choosing a letter randomly
    print(hangmanpics[-lives])
    letter=input('enter a letter: ')
    clear()

    # step 4: Checking if the letter is in the word
    ## Yes
    for i in range(len(word)):
        if letter==word[i]:
            blank[i]=letter
            print('Nice job.')

    ## No
    if letter not in word:
        print('No match :( You lose a life.')
        lives-=1


    print(f'You still have {lives} lives to complete {blank}')

    # Ending the game
    if '_' not in blank:
        print(f'You win')
        continue_game = False

    if lives==0:
        print('Game Over')
        continue_game=False



