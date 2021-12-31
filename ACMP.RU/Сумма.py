with open('ACMP.RU\input.txt', 'r') as file:
        a = int(file.readline())
        if a < 0: print(sum(range(a, 2)))
        elif a > 0: print(sum(range(1, a+1)))
        else: print(1)