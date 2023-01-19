import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
score_board=Scoreboard()

screen.listen()
screen.onkey(player.go_up,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    score_board.update_score()

    #Detecting collision with car
    for car in car_manager.all_cars:

        if car.distance(player)<20:
            print('Collision')
            game_is_on=False
            score_board.clear()
            score_board.game_over()

    if player.sucessful_crossing():
        player.go_to_start()
        score_board.update_score()
        car_manager.level_up()
        score_board.increase_level()
        score_board.update_score()


screen.exitonclick()
