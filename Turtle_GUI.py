
import random

from turtle import Turtle, Screen, colormode
timmy = Turtle()
screen = Screen()
colormode = colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
direction = [0, 90, 180, 270]
timmy.shape('turtle')

timmy.color('red')

for i in range(4):
    timmy.left(90)
    timmy.forward(100)

for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.right(angle)
        timmy.forward(100)


for sides in range(3, 11):
    timmy.color(random.choice(colours))
    draw(sides)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    timmy.pensize(15)
    timmy.speed('fast')
    for _ in range(200):
        timmy.color(random_color())
        timmy.setheading(random.choice(direction))
        timmy.forward(50)


random_walk()


def draw_spirograph(heading_tilt):
    timmy.speed('fastest')
    for _ in range(int(360 / heading_tilt)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + heading_tilt)


draw_spirograph(5)

screen.exitonclick()
