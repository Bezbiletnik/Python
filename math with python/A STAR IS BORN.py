from turtle import *

shape('turtle')
speed(100)

def star(side_length):
    for _ in range(5):
        forward(side_length)
        right(144)

def starSpiral(side_length=5):
    for _ in range(60):
        star(side_length)
        right(5)
        side_length += 5

starSpiral()

input()
