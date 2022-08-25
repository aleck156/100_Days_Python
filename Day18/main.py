import random
from turtle import Turtle as t, Screen

timmy = t()
timmy.shape('turtle')

def random_color_tuple():
    return (random.random(), random.random(), random.random())

def random_direction():
    return random.randint(0, 3)

def draw_shape(num_sides):
    timmy.pencolor(random_color_tuple())
    angle = 360 / num_sides
    for __ in range(0, num_sides):
        timmy.forward(100)
        timmy.left(angle)


for _ in range(1,100):
    color = random_color_tuple()
    direction = random_direction()
    timmy.pencolor(color)
    timmy.left(90*direction)
    timmy.forward(30)

timmy.screen.exitonclick()


# for shapes in range(3,10):
#     draw_shape(shapes)




# for _ in range(5):
#     timmy.forward(100)
#     timmy.left(90)

