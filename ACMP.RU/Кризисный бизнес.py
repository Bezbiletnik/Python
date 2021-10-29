with open('ACMP.RU\input.txt', 'r') as file:
    a, b = file.read().splitlines()
    a = [int(x) for x in a.split()]; b = sorted([int(x) for x in b.split()])
    sumx = 0
    count = 0
    for x in range(a[0]):
        sumx += b[x]
        count += 1
        if sumx > a[1]:
            sumx -= b[x]
            count -= 1
            break
print(sumx)
with open('ACMP.RU\output.txt', 'w') as f:
    f.write(str(count))