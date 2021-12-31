'''
    Program for calculating two coprime integers
'''


from math import gcd

a, b = map(int, input('Enter two numbers __format(a b)__: ').split())
print('The numbers are coprime integers!' if gcd(a,b) == 1 else 'The numbers are not coprime integers!')