import random
from turtle import Turtle as t, Screen
from painting import extract_colors

timmy = t()
timmy.shape('turtle')
color_palette = extract_colors('./damienhirst1.jpg', 10)
screen = Screen()
screen.colormode(255)

def pick_random_color(colors):
    return colors[random.randint(0, len(colors)-1)]

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

def draw_circles(turtle, number):
    for _ in range(0, number):
        color = random_color_tuple()
        turtle.pencolor(color)
        turtle.circle(50)
        turtle.left(360/number)


def draw_dot(turtle, colors):
    turtle.pendown()
    turtle.dot(25, pick_random_color(colors))
    turtle.penup()
def move_matrix(turtle, size, colors):
    left_sign = -1
    angle = 90
    distance = 50
    turtle.penup()
    for _ in range(0, size):
        for __ in range(1, size):
            draw_dot(turtle, colors)
            turtle.forward(distance)
        draw_dot(turtle, colors)
        turtle.left(angle)
        turtle.forward(distance)
        turtle.left(angle)
        angle *= left_sign

move_matrix(timmy, 10, color_palette)
# draw_circles(timmy, 10)

screen.exitonclick()



# for _ in range(1,100):
#     color = random_color_tuple()
#     direction = random_direction()
#     timmy.pencolor(color)
#     timmy.pensize(15)
#     timmy.left(90*direction)
#     timmy.forward(30)



# for shapes in range(3,10):
#     draw_shape(shapes)




# for _ in range(5):
#     timmy.forward(100)
#     timmy.left(90)

