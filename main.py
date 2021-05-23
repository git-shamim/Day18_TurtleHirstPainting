
import random
from turtle import Turtle, Screen, colormode

tim = Turtle()
screen = Screen()
colormode = colormode(255)

color_list = [(244, 213, 94), (60, 98, 151), (222, 142, 75), (125, 84, 57), (123, 174, 206), (199, 147, 174),
              (144, 72, 101), (200, 78, 112), (155, 135, 66), (231, 88, 60), (139, 189, 139), (47, 166, 117),
              (73, 106, 92), (230, 162, 186), (27, 164, 190), (113, 124, 146), (183, 23, 43), (19, 64, 125),
              (15, 53, 94), (168, 192, 221), (158, 206, 219), (159, 213, 182), (235, 220, 10), (200, 22, 12),
              (76, 59, 41), (81, 64, 41)]

tim.speed('fastest')
tim.penup()
tim.hideturtle()

tim.setheading(to_angle=225)
tim.forward(300)
tim.setheading(to_angle=0)

dots = 100
for dot in range(1, dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(to_angle=90)
        tim.forward(50)
        tim.setheading(to_angle=180)
        tim.forward(500)
        tim.setheading(to_angle=0)

screen.exitonclick()
