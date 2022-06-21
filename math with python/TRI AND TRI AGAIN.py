from turtle import *

shape('turtle')
speed(100)

def triangle(side_length: int):
    for _ in range(3):
        forward(side_length)
        left(120)

for _ in range(72):
    triangle(150)
    right(5)

input()
