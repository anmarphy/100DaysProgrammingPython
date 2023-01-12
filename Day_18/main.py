from turtle import *
from random import *

timmy=Turtle()
timmy.shape('turtle')
timmy.color('orange')

# TODO:Challenge 1: Square
# TODO: Challenge 2: dash line
def square():
    for _ in range(4):
        for _ in range(20):
            timmy.forward(5)
            timmy.penup()
            timmy.forward(5)
            timmy.pendown()
        timmy.right(90)
square()

# TODO: Challenge 3: Shapes
def n_shapes(n):
    for i in range(3,n+1):
        sides=i
        angle=360/sides
        lenght=100

        for _ in range(sides):
            r = uniform(0, 1)
            g = uniform(0, 1)
            b = uniform(0, 1)
            tup = (r, g, b)
            timmy.pencolor(tup)
            timmy.forward(lenght)
            timmy.right(angle)
#n_shapes(5)

# TODO: Generate a random walk
def random_walk(n):
    for _ in range(n):
        angle=randint(0,360)
        length=randint(20,100)
        timmy.pensize(3)
        timmy.shapesize(1)
        timmy.forward(length)
        timmy.right(angle)
#random_walk(30)

# TODO: Spirograph
def spirograph(n):
    for _ in range(n):
        timmy.speed('fastest')
        r = uniform(0, 1)
        g = uniform(0, 1)
        b = uniform(0, 1)
        tup = (r, g, b)
        timmy.pencolor(tup)
        timmy.circle(radius=100)
        current_heading=timmy.heading()
        timmy.setheading(current_heading+(360/n))
#spirograph(100)


screen = Screen()
screen.exitonclick()