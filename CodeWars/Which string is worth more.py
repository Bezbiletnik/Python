'''My solution'''


def highest_value(a, b):
    sum_a, sum_b = sum([ord(x) for x in a]), sum([ord(x) for x in b])
    return a if sum_a >= sum_b else b

print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"))


'''Best practices'''
def highest_value(a, b):
    return max(a, b, key=lambda s: sum(map(ord, s)))