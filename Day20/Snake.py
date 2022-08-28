from turtle import Turtle

class Snake:
    def __init__(self, size):
        self.snake = []
        self.create_snake(self.snake, size)

    def create_snake(self, snake, size):
        for index in range(0, size):
            new_snake_part = Turtle(shape='square')
            new_snake_part.penup()
            new_snake_part.goto(index * (-20), 0)
            new_snake_part.color('white')
            snake.append(new_snake_part)

    def __len__(self):
        return len(self.snake)