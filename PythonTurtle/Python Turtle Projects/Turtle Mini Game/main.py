from turtle import *

bgcolor("Orange")

move_distance = 20

color("blue")
begin_fill()

penup()
goto(100, 200)
pendown()

goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

penup()
goto(-200, 0)
color("green")
shape("turtle")

def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(-90)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(-180)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(360)
    forward(move_distance)
    check_goal()

def check_goal():
    if xcor() > 100:
        hideturtle()
        color("White")
        write("You Win!")
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()



done()