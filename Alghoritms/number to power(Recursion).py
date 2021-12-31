# def power(a, n):
#     return 1 if n == 0 else power(a, n-1) * a


#Faster function
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0: # for even numbers
        return power(a**2, n/2)
    else:
        return power(a, n-1) * a


print(power(2, 1024)) #Result: 8