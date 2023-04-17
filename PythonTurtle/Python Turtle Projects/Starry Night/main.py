from turtle import *
from random import *

speed(0)

bgcolor("Black")
hideturtle()

# Variables
width = window_width()
height = window_height()
maxStars = 100

def draw_star(xpos, ypos):
    size = randrange(7, 14)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

for x in range(maxStars):
   xpos = randrange(round(-width / 2), round(width / 2))
   ypos = randrange(round(-height / 2), round(height / 2))
   draw_star(xpos, ypos)

done ()

