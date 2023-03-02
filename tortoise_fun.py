import turtle
from turtle import *
import random

color("darkblue", "lightblue")

begin_fill()
alex = turtle.Turtle()
angle = random.randint(1, 179)
print(angle)
distance = 200
while True:
    alex.speed(10)
    alex.forward(distance)
    alex.left(angle)
end_fill()
done()
