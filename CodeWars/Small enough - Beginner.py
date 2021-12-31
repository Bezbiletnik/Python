'''My solution'''


def small_enough(array, limit):
    return all(i <= limit for i in array)


'''Best practices'''


def small_enough(array, limit):
    return max(array)<=limit