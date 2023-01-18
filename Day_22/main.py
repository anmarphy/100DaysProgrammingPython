from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball=Ball()
score=Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()



    #Detecting collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detecting collision with right
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #Detecting missing balls
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()