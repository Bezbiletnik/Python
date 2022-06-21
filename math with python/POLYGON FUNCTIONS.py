from turtle import *

shape('turtle')
speed(100)

def polygon(side_length: int, amount: int):
    for _ in range(amount):
        forward(side_length)
        left(360/amount)

for _ in range(72):
    polygon(150, 12)
    right(5)
input()
