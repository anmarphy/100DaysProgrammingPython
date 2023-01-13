import turtle
from turtle import Screen, Turtle
import random

is_race_on=False
screen=Screen()
width=500
height=400
screen.setup(width, height)

user_bet=screen.textinput(title='make your bet', prompt='Which turtle? Enter a color: ')
colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles=[]

for i in range(6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-width/2, y=-height/4 + 50 * i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> width/2:
            is_race_on=False
            winning_color=turtle.color()
            if winning_color==user_bet:
                print(f'You won.')
            else:
                print(f'You lose.')
            print(f'The {winning_color[0]} turtle is the winner')

        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()