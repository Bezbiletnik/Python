array = ['Apple', 'Google', 'Facebook', 'Amazon', 'Netflix']
element = 'Facebook'

#array2 = sorted(array)

# Only for sorted arrays
def findindex(array, element):
    l, r = 0, len(array) - 1
    while l <= r:
        m = l + (r - l) // 2
        if array[m] == element:
            return m
        elif array[m] < element:
            l = m + 1
        else: r = m - 1
    return "element isn't in array"

def findindex(array, element):
    for i, el in enumerate(array):
        if el == element:
            return i
    return "Element isn't in array"

print(findindex(array, element))

