with open('ACMP.RU\input.txt', 'r') as file:
    a, b = file.read().splitlines()
    odd =  []; even = []
    for i in b.split():
        if int(i) % 2 != 0: odd.append(i)
        else: even.append(i)
    print(' '.join(odd)); print(' '.join(even))
    print('YES' if len(odd)<=len(even) else 'NO')