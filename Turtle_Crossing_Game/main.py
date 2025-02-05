import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    if random.randint(1, 8) ==1:
        car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.reset_position()
        car_manager.car_increase()
        scoreboard.increase_score()

    if player.car_collision(car_manager.all_cars):
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()

