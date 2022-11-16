import turtle
from turtle import Turtle,Screen
import random
t1=Turtle()
t1.shape("turtle")
t1.penup()
t1.setposition(-50,70)
t1.pendown()
t1.color("blue")
color=["brown","dark olive green","pink","dark turquoise","medium slate blue","dark orange"]
for i in range(3,11):
    angle=360/i
    t1.color(random.choice(color))
    for i2 in range (1,i+1) :
        t1.forward(120)
        t1.right(angle)
