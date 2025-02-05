from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.turtlesize(1, 2)
        new_car.setheading(180)
        new_car.goto(x = 300, y = random.randint(-300, 300))
        self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def car_increase(self):
        self.car_speed += MOVE_INCREMENT


