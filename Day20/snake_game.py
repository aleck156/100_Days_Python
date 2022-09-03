import time
from turtle import Turtle, Screen

from Day20.Scoreboard import Scoreboard
from Food import Food
from Snake import Snake


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
speed = 0.1
screen = Screen()

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

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
screen.onkey(screen.bye, 'space')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 25:
        food.refresh()
        scoreboard.add_point()
        snake.extend()

    if (snake.head.xcor() > SCREEN_WIDTH / 2 - 25) or (snake.head.xcor() < -SCREEN_WIDTH / 2 + 25) or (snake.head.ycor() > SCREEN_HEIGHT / 2 - 25) or (snake.head.ycor() < -SCREEN_HEIGHT / 2 + 25):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
