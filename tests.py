# from collections import Counter

# numbers = [1, 1, 2, 3, 3, 3, 4, 4, 5, 5]
# with open('text.txt', 'r', encoding='UTF-8') as file:
#     list1 = list(file.read().split())
#     print(list1)


# def not_most_common(list):
#     return min(set(list), key=list.count)

# print(not_most_common(list1))

# print('%.3f' % (1/2))
# result = round((4/3), 3)
# print(result)
# import sys


# def expenses():
#     value = 0
#     print('Enter your new expense')
#     try:
#         value = int(input())
#     except ValueError:
#         print('You entered incorrect value!')
#     return value


# def income():
#     value = 0
#     print('Enter your new income')
#     try:
#         value = int(input())
#     except ValueError:
#         print('You entered incorrect value!')
#     return value


# def initial_capital():
#     capital = 0
#     print('Enter your new initial capital')
#     try:
#         capital = int(input())
#     except ValueError:
#         print('You entered incorrect value!')
#     return capital


# def user_exit():
#     sys.exit(0)


# def select_category(argument):
#     switcher = {
#         1: expenses,
#         2: income,
#         3: initial_capital,
#         4: user_exit
#     }

#     return switcher.get(argument, 'Invalid value')

# output = select_category(3)
# output()
# import os

# n = 0

# def enter():
#     try:
#         print("Сколько случайных чисел должна создать программа?")
#         n = int(input("> "))
#         if n < 5:
#             os.system('cls||clear')
#             print("Желательно ввести число больше 5, иначе анализ будет весьма неточным")
#             enter()
#     except:
#         os.system('cls||clear')
#         print("Ошибка ввода")
#         enter()
#     return print(n)
