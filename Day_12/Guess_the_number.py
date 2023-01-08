from art import logo
from random import choice

range_number=[i for i in range(0,101)]



def guess_number():
    print(logo)

    number_to_guess=choice(range_number)
    #print(f'The correct answer is: {number_to_guess}')

    level=input('💡 Choose the level: Easy or Hard  ')

    if level=='Easy':
        attempts=10

    elif level=='Hard':
        attempts=5
    else:
        print('That is not a valid level')
        level = input('Choose the level: Easy or Hard ')

    print(f'You have {attempts} attempts on level {level.lower()}')

    while attempts >0:
        guess=int(input('Make your guess: '))

        if guess>number_to_guess:
            print('Too High \nGuess again')
            attempts-=1
            print(f'You still have {attempts}')
        elif guess <number_to_guess:
            print('Too Low \nGuess again')
            attempts -= 1
            print(f'You still have {attempts}')
        else:
            print(f'You got it!! 🎉🎉🎉')
            attempts=0

    if attempts==0:
        print('End Game 😵‍💫')
        print(f'The answer was {number_to_guess}')
        should_continue=input('Do you want to play again? Yes or No ')
        if should_continue=='Yes':
            guess_number()
        else:
            print('See You Soon! 👋👋👋 ')

guess_number()