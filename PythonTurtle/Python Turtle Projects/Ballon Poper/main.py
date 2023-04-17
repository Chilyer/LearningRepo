from turtle import *

diameter = 40
pop_diameter = 250

def draw_balloon ():
    color("Red")
    dot(diameter)

def inflate_ballon():
    global diameter
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("Pop!")

draw_balloon()

onkey(inflate_ballon, "Up")
listen()

done()
