def fib_digit(n):
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, (a+b)%10
    return b


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()