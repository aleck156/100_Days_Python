import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.hideturtle()
        self.cars = []
        for index in range(0,10):
            self.cars.append(self.new_car())

    def new_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape('square')
        new_car.left(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(COLORS[random.randint(0, len(COLORS) - 1)])
        new_car.goto(random.randint(0,600) - 300, random.randint(0, 600) - 300)
        return new_car

