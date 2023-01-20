#Day 17
from turtle import Turtle, Screen
import random

caroline = Turtle()
caroline.shape("turtle")
caroline.color("green")
caroline.speed("fastest")
caroline.pensize(15)

colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "white", "grey"]

# Defining a method to draw curve
def curve():
    for i in range(200):
        caroline.color(random.choice(colours))
        # Defining step by step curve motion
        caroline.right(1)
        caroline.forward(1)
  
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    caroline.color(random.choice(colours))
  
    # Start filling the color
    caroline.begin_fill()
  
    # Draw the left line
    caroline.left(140)
    caroline.forward(113)
  
    # Draw the left curve
    curve()
    caroline.left(120)
  
    # Draw the right curve
    curve()
  
    # Draw the right line
    caroline.forward(112)
  

my_screen = Screen()
print(my_screen.canvheight)
heart()
my_screen.exitonclick()


