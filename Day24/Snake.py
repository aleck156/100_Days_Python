import time
from turtle import Turtle

MOVE_DISTANCE = 20
class Snake:
    def __init__(self, size):
        self.snake = []
        self.create_snake(size)
        self.head = self.snake[0]

    def __len__(self):
        return len(self.snake)
    def create_snake(self, size):
        for index in range(0, size):
            self.add_snake_part(index)


    def add_snake_part(self, position):
        new_snake_part = Turtle(shape='square')
        new_snake_part.penup()
        new_snake_part.goto(position * (-20), position * 0)
        new_snake_part.color('white')
        self.snake.append(new_snake_part)

    def extend(self):
        self.add_snake_part(self.snake[-1].xcor())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
