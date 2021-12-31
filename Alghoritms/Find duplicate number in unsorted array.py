# import random
# # Generator 
# a = list()
# N = 10
# for _ in range(N+1):
#     a.append(random.randint(1, N+1))


A = [7, 3, 5, 3, 3, 9, 4, 4, 8, 11, 3] # Expected 3


unique = list()
for i in A:
    if i not in unique:
        unique.append(i)
    else:
        print(i, end=' ')