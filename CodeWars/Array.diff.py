'''
    My solution(helped)
'''


def array_diff(a, b):
    for val in range(len(b)):
        while b[val] in a:
            a.remove(b[val])
    return a


print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2], [2]))
print(array_diff([1,2,3], [1, 2]))


'''
    Best Practices:


    def array_diff(a, b):
    return [x for x in a if x not in b]

'''