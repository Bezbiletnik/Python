from turtle import *
shape('turtle')
speed(20)
def square(side_length: int):
    for _ in range(4):
        forward(side_length)
        right(90)

for _ in range(75):
    square(150)
    right(5)
input()
