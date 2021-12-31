array = ['Apple', 'Google', 'Facebook', 'Amazon', 'Netflix']
element = 'Facebook'


# Only for sorted arrays
def findindex(array, element):
    if element in array:
        l, r = 0, len(array) - 1
        while l < r:
            m = l + (r - l) // 2
            if array[m] == element:
                return m
            elif array[m] < element:
                l += 1
            else: r -= 1
    return "element isn't in array"


# Solution
def findindex(array, element):
    for i, j in enumerate(array):
        if j == element:
            return i
    return "element is't in array"


print(findindex(array, element))