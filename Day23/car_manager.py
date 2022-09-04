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
            self.cars.append(self.new_car(random.randint(0,500) - 250,random.randint(0,500) - 250))

    def new_car(self, x_cor, y_cor):
        new_car = Turtle()
        new_car.penup()
        new_car.shape('square')
        new_car.left(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(COLORS[random.randint(0, len(COLORS) - 1)])
        new_car.goto(x_cor, y_cor)
        return new_car

    def move_all_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def stop_all_cars(self):
        for car in self.cars:
            car.forward(0)

    def remove_unseen_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)
                self.cars.append(self.new_car(300, random.randint(0,500) - 250))

    def collision_detection(self, turtle):
        for car in self.cars:
            if car.distance(turtle.pos()) < 30:
                return True
