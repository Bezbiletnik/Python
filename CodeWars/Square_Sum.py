'''My solution'''
list1 = []
result = 0
for i in range(0, len(list1)):
    result = (list1[i]**2) + result
print(result)

'''Most popular solution'''
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)
'''
Definition and Usage:
    The sum() function returns a number, the sum of all items in an iterable.
Syntax:
    sum(iterable, start)
Parameter Values:
    Parameter	Description
    iterable	Required. The sequence to sum
    start	    Optional. A value that is added to the return value
Exapmle:
    a = (1, 2, 3, 4, 5)
    x = sum(a, 7)
    print(x), here function print() returns 22.
'''
