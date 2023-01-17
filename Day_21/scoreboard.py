from turtle import Turtle
ALIGMENT='center'
FONT=('Arial', 14, 'normal')

class Scoreboard(Turtle):
    def update_score(self):
        self.write(f'Score {self.score}', align=ALIGMENT, font=FONT)

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score=0
        self.penup()
        self.goto(0, 220)
        self.update_score()
        self.hideturtle()


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over', align=ALIGMENT, font=FONT)
