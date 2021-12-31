'''
    Program for checking "random" module in python
'''

# Friday, October 29, 2021
n = 0


def enter():
    global n
    try:
        print('Сколько случайных чисел должна создать программа?')
        n = int(input('> '))
        if n < 5:
            system('cls||clear')
            print("Желательно ввести число больше 5, иначе анализ будет весьма неточным")
            enter()
    except ValueError:
        system('cls||clear')
        print('Ошибка ввода')
        enter()


def main():
    again = 'y'
    while again == 'y':
        enter()
        start = time()
        count = [0] * 10
        for _ in range(n):
            numeral = randint(1, 10)
            count[numeral-1] += 1

        end = time()
        results = [(i + 1, f'{(count[i]/n*100):.2f} %', count[i]) for i in range(10)]
        print(
            '\nВсего было создано %d случайных чисел' % n,
            '\nАнализ выполнился за %.2f секунд\n' % (end - start)
        )
        print(tabulate(results, headers=['Number', 'Percent', 'Quantity'], tablefmt='grid'))
        print('\nХотите ли вы продолжить?(y/n)')
        again = input('> ').lower()
        system('cls||clear')

if __name__ == '__main__':

    from random import randint
    from time import time
    from os import system

    from tabulate import tabulate

    main()

# Tuesday, December 28, 2021
# Dictionary, works a bit slower, but I will fix that
n = 0


def enter():
    global n
    try:
        print('Сколько случайных чисел должна создать программа?')
        n = int(input('> '))
        if n < 5:
            system('cls||clear')
            print("Желательно ввести число больше 5, иначе анализ будет весьма неточным")
            enter()
    except ValueError:
        system('cls||clear')
        print('Ошибка ввода')
        enter()


def main():
    again = 'y'
    while again == 'y':
        enter()
        start = time()
        count = dict()
        for _ in range(n):
            numeral = randint(1, 10)
            if numeral not in count: count[numeral] = 1
            else: count[numeral] += 1

        end = time()
        results = [(i, f'{(count[i]/n*100):.2f} %', count[i]) for i in range(1, 11)]
        print(
            '\nВсего было создано %d случайных чисел' % n,
            '\nАнализ выполнился за %.2f секунд\n' % (end - start)
        )
        print(tabulate(results, headers=['Number', 'Percent', 'Quantity'], tablefmt="grid"))
        print('\nХотите ли вы продолжить?(y/n)')
        again = input('> ').lower()
        system('cls||clear')

if __name__ == '__main__':

    from random import randint
    from time import time
    from os import system

    from tabulate import tabulate

    main()