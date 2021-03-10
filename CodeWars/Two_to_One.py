'''My solution'''
'''
What I used:
    list() function - creates list from string,
    set() function - deletes repetitive values,
    sort() function - sorts the elements of a given list in a specific ascending or descending order.
'''
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
result = list(set(a+b))
result.sort()
print(''.join(result))

'''Most popular solution'''
# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))
'''
Definition and Usage:
    The sorted() function returns a sorted list of the specified iterable object.
    You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
Syntax:
    sorted(iterable, key=key, reverse=reverse)
Parameter Values:
    Parameter	Description
    iterable	Required. The sequence to sort, list, dictionary, tuple etc.
    key	        Optional. A Function to execute to decide the order. Default is None
    reverse	    Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
'''