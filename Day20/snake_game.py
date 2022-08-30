import time
from turtle import Turtle, Screen

from Food import Food
from Snake import Snake


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
speed = 0.1
screen = Screen()

snake = Snake(3)
food = Food()

screen.tracer(0)
# screen.update()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title('Welcome to the SNAKE GAME')
screen.bgcolor('black')
screen.colormode(255)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 25:
        food.refresh()

screen.exitonclick()
