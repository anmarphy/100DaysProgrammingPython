import colorgram as cg
import numpy as np
from turtle import *
import random

def my_painting(n, l, file):
    colormode(255)
    color_list = cg.extract(file,40)
    rgb_colors = []

    for coloring in color_list:
        r = coloring.rgb.r
        g = coloring.rgb.g
        b = coloring.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    tim = Turtle()
    tim.speed('fastest')

    for dot_count in range(1, n + 1):
        tim.dot(20, random.choice(rgb_colors))
        tim.hideturtle()
        tim.penup()
        tim.forward(l)

        if dot_count % np.sqrt(n) == 0:
            tim.setheading(90)
            tim.forward(l)
            tim.setheading(180)
            tim.forward(np.sqrt(n)*l)
            tim.setheading(0)

my_painting(100,40, "Vg.JPG")

screen = Screen()
screen.exitonclick()