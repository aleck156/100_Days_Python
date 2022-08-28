import time
from turtle import Turtle

class Snake:
    def __init__(self, size):
        self.snake = []
        self.create_snake(size)

    def create_snake(self, size):
        for index in range(0, size):
            new_snake_part = Turtle(shape='square')
            new_snake_part.penup()
            new_snake_part.goto(index * (-20), 0)
            new_snake_part.color('white')
            self.snake.append(new_snake_part)

    def move(self, screen):
        for _ in range(0, ):
            screen.delay(5)
            for seg_num in range(len(self.snake) - 1, 0, -1):
                new_x = self.snake[seg_num - 1].xcor()
                new_y = self.snake[seg_num - 1].ycor()
                self.snake[seg_num].goto(new_x, new_y)
            self.snake[0].forward(20)
            time.sleep(1)
            screen.update()

    def __len__(self):
        return len(self.snake)