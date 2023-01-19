from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.color('blue')
        self.penup()
        self.goto(-200, 200)


    def increase_level(self):
        self.level+=1


    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='right', font=FONT)


