def gcf(a: int, b: int):
    if a == 0:
        return b
    if b == 0:
        return a
    if a <= b:
        return gcf(a, b % a)
    else:
        return gcf(a % b, b)

print(gcf(150, 138))
