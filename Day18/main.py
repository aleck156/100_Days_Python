from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)


timmy.screen.exitonclick()
