#Spirograph with turtle and random color

from turtle import Turtle, Screen
import random

caroline = Turtle()
caroline.shape("turtle")
caroline.color("green")
r = random.rand



def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        caroline.color(random.choice(colours))
        caroline.circle(100)
        caroline.setheading(caroline.heading() + size_of_gap)

