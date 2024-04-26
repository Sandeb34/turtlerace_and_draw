# https://docs.python.org/3/library/turtle.html
# Use your keyboard to make a drawing in turtle look for the keys below:
from turtle import Turtle, Screen

# creating two objects from turtle class
billy = Turtle()
screen = Screen()


def move_forward():
    """Turtle moves 10 spaces forward. Function for screen.onkey Method"""
    billy.forward(10)


def move_backward():
    """Turtle moves 10 spaces backward. Function for screen.onkey Method"""
    billy.backward(10)


def move_counterclockwise():
    billy.left(10)


def move_clockwise():
    billy.right(10)


def clearscreen():
    """Hopefully clears screen"""
    billy.reset()

# Allow user to control turtle with keystrokes.
screen.listen()
# Controls for moving the turtle.
# w = forward
# s = backward
# a = counterclockwise
# d = clockwise
# c - clear drawing

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clearscreen)
screen.exitonclick()


