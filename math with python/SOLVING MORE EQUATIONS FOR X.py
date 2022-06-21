def solve_equation(a,b,c,d):
    '''solves equations of the form ax + b = cx + d'''
    return (d - b)/(a - c)

print(solve_equation(1/2, 2/3, 1/5, 7/8))
