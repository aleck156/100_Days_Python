import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, 'Up')
screen.onkey(screen.bye, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_manager.collision_detection(player):
        car_manager.stop_all_cars()
        scoreboard.game_over()
    else:
        car_manager.move_all_cars()
        car_manager.remove_unseen_cars()


    if player.ycor() > 280:
        scoreboard.update_score()
        player.restart_position()
