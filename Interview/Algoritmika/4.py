# First solution
N = 13
for i in range(1, N+1, 2):
    print(f'{"*" * i}'.center(N+1))

# Second solution
N = 13
for i in range(1, N+1, 2):
    spaces = ' ' * ((N - i)//2)
    print(spaces + '*' * i + spaces)
