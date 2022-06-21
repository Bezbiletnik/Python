from math import sqrt

def quad(a,b,c):
    '''Return the solutions of an equation for the form ax**2 + bx + c = 0'''
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

a,b,c = map(int, input('Write the coefficients of the equation: ').split())
print(quad(a,b,c))
