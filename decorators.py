import time


def testTime(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time() - start
        print(f'Время работы: {end} сек')
        return res
    return wrapper

@testTime
def getNOD(a, b):
    while a!= b:
        if a > b: a -= b
        else: b -= a
    return a


res = getNOD(10000 , 2)
print(res)
