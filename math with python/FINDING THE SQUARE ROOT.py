def average(a, b):
    return (a+b)/2

def squareRoot(number, low, high):
    guess = -1
    for _ in range(100):
        guess = average(low, high)
        if guess**2 == number:
            break
        elif guess**2 > number:
            high = guess
        else:
            low = guess
    print(guess)

squareRoot(1000, 1, 10000)
