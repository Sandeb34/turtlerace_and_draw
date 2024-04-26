import turtle
from turtle import Turtle, Screen
import random

# Set flag for while loop.
is_race_on = False
screen = Screen()
screen.setup(500,400)

# Popup question in turtle
user_bet = screen.textinput("Make your bed","Which turtle will win the race? Enter the color:")
print(user_bet)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# starting Y-coordinate for the 6 starting turtles
y_positions = [-70, -40, -10, 20, 50, 80]

# New turtles will be added here.
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    # takes the colors from the list
    new_turtle.color(colors[turtle_index])
    # the end of the screen is 250 but turtles will not be visible therefor 230
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Use the flag from the beginning
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # the turtle is 40px by 40px the end of the screen is 250 - (40/2) = finish line at y:230
        if turtle.xcor() > 230:
            # Game is over after the first turtle reaches the finish line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won.The winner is {winning_color}")
            else:
                print(f"You've lost.The winner is {winning_color}")

        # creates a random number which is the speed of the turtles.
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()