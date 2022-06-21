def main(n):
    d, nRemainder = 1, 0
    length = len(str(n))
    while(length):
        nRemainder = (n // d) % 10
        if nRemainder == 2:
            return True
        d *= 10; length -= 1
    return False


n = int(input('Enter the number: '))
print(main(n))
