from random import randint

# with open('Some_random_tasks\input.txt', 'w') as f:
#     for i in range(50):
#         f.write('{}\n'.format(str(randint(1, 150))))


with open('Some_random_tasks\input.txt', 'r') as f:
        a = list(map(int, f))
        print(list(filter(lambda x: x%2!=0, a)))