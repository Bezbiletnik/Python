from turtle import *
shape('turtle')

def square():
    '''Function for creating square'''
    for _ in range(4):
        forward(100)
        left(90)

square()
print(square.__doc__)
input()
