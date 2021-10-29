with open('ACMP.RU\INPUT.TXT', 'r') as file:
    n, a, b = [int(x) for x in file.readline().split()]
    result = 2 * (n * (a*b))
with open('ACMP.RU\OUTPUT.TXT', 'w') as f:
    f.write(str(result))