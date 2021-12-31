a = 'Алгоритмика'
b = [x for x in a]
element = 'р'


def search_element(array, element):
    for i, j in enumerate(b):
        if j == element:
            return i
    return -1


print(search_element(b, element))