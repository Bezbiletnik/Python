# import random

# Generator
# a = []
# for _ in range(20):
#     a.append(random.randint(1, 50))

# print(a)

a = [45, 20, 13, 50, 27, 36, 33, 49, 18, 31, 24, 20, 41, 20, 22, 9, 34, 14, 26, 44]

# Modified bubble sort, because usual bubble sort was not optimum
def bubble_sort(a):
    changed = True
    while changed:
        changed = False
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                changed = True


bubble_sort(a)
print(a)
