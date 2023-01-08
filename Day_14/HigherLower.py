from art import *
from game_data import data
import random

def formatted_data(index):
    name= data[index]['name']
    info= data[index]['description']
    return f'{name} : {info}'


def higher_lower():

    score = 0
    should_continue = True
    num_a = random.randint(0, len(data))

    while should_continue==True:

        num_b= random.randint(0,len(data))

        print(f'Opt A:{formatted_data(num_a)}')
        print(vs)
        print(f'Opt B: {formatted_data(num_b)}')
        rule=input('Who has more followers? A or B ')

        def comparision(num_a, num_b):
            followers_a = data[num_a]['follower_count']
            followers_b = data[num_b]['follower_count']

            if followers_a>followers_b:
                return num_a
            else:
                return num_b

        if rule=='A' and comparision(num_a, num_b)==num_a:
            score+=1
            print(f'You are right. Your current score is {score} ')
        elif rule=='B' and comparision(num_a, num_b)==num_b:
            score+=1
            print(f'You are right. Your current score is {score}')
            num_a=num_b
        else:
            print(f'Sorry. That is wrong. Your score is {score}')
            checking=input('Do you want to continue playing? Yes or No')
            if checking=='Yes':
                should_continue=True
                higher_lower()
            else:
                should_continue = False
                print('See you soon!!')

print(logo)
higher_lower()


