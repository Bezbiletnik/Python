from turtle import *

shape('turtle')
speed(100)

def spiral(side_length=5):
    for _ in range(60):
        for _ in range(4):
            forward(side_length)
            left(90)
        side_length += 5
        left(5)
            
spiral()
input()

