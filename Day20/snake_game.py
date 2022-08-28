import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

speed = 1
screen = Screen()

snake = Snake(3)

screen.tracer(0)
# screen.update()

screen.setup(width=1600, height=1200)
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

screen.exitonclick()
