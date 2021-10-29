'''
    Program for checking "random" module in python
'''

# Friday, October 29, 2021
# Refactoring
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
        for i in range(n):
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

# n = 0


# def enter():
#     # Function for user input
#     global n
#     try:
#         print("Сколько случайных чисел должна создать программа?")
#         n = int(input("> "))
#         if n < 5:
#             system('cls||clear')
#             print("Желательно ввести число больше 5, иначе анализ будет весьма неточным")
#             enter()
#     except ValueError:
#         system('cls||clear')
#         print("Ошибка ввода")
#         enter()


# def main():
#     # Main function
#     again = 'д'
#     while again == 'д':
#         enter()
#         start = time()
#         count1 = count2 = count3 = count4 = count5 = \
#         count6 = count7 = count8 = count9 = count10 = 0

#         for i in range(n):
#             numeral = randint(1, 10)
#             if numeral == 1:
#                 count1 += 1
#             elif numeral == 2:
#                 count2 += 1
#             elif numeral == 3:
#                 count3 += 1
#             elif numeral == 4:
#                 count4 += 1
#             elif numeral == 5:
#                 count5 += 1
#             elif numeral == 6:
#                 count6 += 1
#             elif numeral == 7:
#                 count7 += 1
#             elif numeral == 8:
#                 count8 += 1
#             elif numeral == 9:
#                 count9 += 1
#             elif numeral == 10:
#                 count10 += 1
#         top = [count1, count2, count3, count4, count5,
#                 count6, count7, count8, count9, count10]
#         end = time()
#         results = [(i + 1, f'{(top[i]/n*100):.2f} %', top[i]) for i in range(10)]
#         print(
#             '\nВсего было создано %d случайных чисел' % n,
#             '\nАнализ выполнился за %.2f секунд\n' % (end - start)
#         )
#         print(tabulate(results, headers=['Number', 'Percent', 'Quantity'], tablefmt='grid'))
#         print('\nХотите ли вы продолжить?(д/н)')
#         again = input('> ').lower()
#         system('cls||clear')

# if __name__ == '__main__':

#     from random import randint
#     from time import time
#     from os import system

#     from tabulate import tabulate

#     main()