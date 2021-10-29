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

# result = 0

# for i in range(1, 283):
#     if len(str(i)) == 1:
#         result = result + 1
#     elif len(str(i)) == 2:
#         result = result + (i % 10) + (int(i / 10))
#     elif len(str(i)) == 3:
#         result = result + ((i % 100) % 10) + (int(i / 100)) + (int((i % 100) / 10))

# print(result)

# import time
# import datetime

# print(time.gmtime())
# print('#' * 30)
# print(datetime.datetime.now('M/d/yyyy h:mm AP'))

# import random

# chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# passwords = []

# for i in range(101):
#     password = ''
#     for i in range(random.randint(7, 9)):
#         password += random.choice(chars)
#     passwords.append(password)

# print(passwords)

# def func(str):
#     if list(str).count('(') == list(str).count(')'):
#         return True
#     return False
#     # dict( (l, list(str).count(l) ) for l in set(str))

# print(func('((())))')) # False

# d = int(input())
# s = 0
# n = 0
# while n < 200:
#   s = s + 64
#   n = n + d
# print(s)

# 25 

# results = []
# for i in range(251811, 251827):
#     for k in range(i):
#         print(k)

# print(results)

# def get_last_elements(a):
#     return [a[0], a[-1]]

# print(get_last_elements([5, 10, 15, 20, 25])) # Result: [5, 25]

# for d in range(1, 100):
#     n = 2
#     s = 0
#     while s <= 365:
#         s = s + d
#         n = n + 5
#         if n == 67 and s >= 365:
#             print('-' * 30)
#             print('d is equal: {}'.format(d))
#             print('s is equal: {}'.format(s))
#             print('n is equal: {}'.format(n))
#             print('-' * 30)

        
# n = 27
# s = 12
# d = int(input('Enter your number: '))
# while s <= 2019:
#     s = s + d
#     n = n + 16
# print(n)


# def title_case(title, minor_words=''):
#     if title == '':
#         return ''
#     new_title = []
#     new_title.append(title.split()[0].capitalize())
#     for word in title.lower().split()[1:]:
#         if word in minor_words.lower().split():
#             new_title.append('{}'.format(word))
#         else:
#             new_title.append('{}'.format(word.capitalize()))
#     return ' '.join(new_title)
        
# print(title_case('', ''))
# print(title_case('a clash of KINGS', 'a an the of'))
# print(title_case('THE WIND IN THE WILLOWS', 'The In'))
# print(title_case('the quick brown fox'))


# A=[10,20,30,40]

# for k in [0,1,2,'три',4,3]:
#     try:
#         print("A["+str(k)+"] = ", end="")
#         A[k]/=(k-1)
#         print(A[k])
#     except IndexError:
#         print("нет такого элемента")
#     except ZeroDivisionError:
#         A[k]=0.0
#         print(A[k],"- деление на ноль")
#     except TypeError:
#         print("Не верный тип индекса")


# while True:
#     res = input('Enter a natural number: ')
#     try:
#         num = int(res)
#         if num < 1:
#             raise ArithmeticError('Number must be a natural')
#         except ArithmeticError as error:
#             print(error)
#         except:
#             print('input error')
#         else:
#             break
#     print('Sum from 1 to {} = {}'.format(num, sum(num+1)))

# import re
# a = [0, 1, 1, 9, 8, 0, 2, 0, 1, 0, 0, 2, 0, 0]

# str = "0, 0, 2, 0, 0"


# with open('input2.txt', 'r') as file:
#     a = file.read().splitlines()
#     # print(a)
#     count = 0
#     a_1 = a[0].split()
#     a_2 = a[1].split()
#     for int(num) in a_2:
#         num += a_1[1]
#         count += 1
#         if count == int(a_1[2]):
#             print(num)
# def func():
#     with open('Input2.txt', 'r') as file:
#         a, b = file.read().splitlines()
#         a, b = int(a), int(b)
#         if a > b:
#             return '>'
#         elif a == b:
#             return '='
#         elif a < b:
#             return '<'
# with open('Output2.txt', 'w') as f:
#     f.write(func())

# with open('input2.txt', 'r') as file:
#     n, m, k = [int(x) for x in file.readline().split()]
#     # print(type(n))
#     if (n*m)>=k:
#         result = 'YES'
#     else: result = 'NO'
# with open('output2.txt', 'w') as f:
#   f.write(result)

# with open('input.txt', 'r') as file:
#     a = file.read().splitlines()
#     strn = ''
#     for i in a[1:]:
#         strn = re.sub(r'(A(w+)?B(w+)?)|(B(w+)?C(w+)?)|(B(w+)?A(w+)?)|(C(w+)?B(w+)?)', '',i)
#         strn = re.sub(r'(A(w+)?B(w+)?)|(B(w+)?C(w+)?)|(B(w+)?A(w+)?)|(C(w+)?B(w+)?)', '',strn)
#         if strn == '':
#             print('YES')
#         else:
#             print('NO')
# import sys

# strn = [x.strip() for x in sys.stdin.readlines()][1:]
# print(strn)
# for k in strn:
#     a, b, c = [k.count(x) for x in ['A', 'B', 'C']]
#     if a + c == b:
#         print('YES')
#     else:
#         print('NO')

# import sys
# s = sys.stdin.read()
# print(s)

# from fractions import Fraction
# import math 

# a = [int(x) for x in input().split('/')]
# b = [int(x) for x in input().split('/')]
# result_1 = Fraction(a[0], a[1])
# result_2 = Fraction(b[0], b[1])
# result = result_1 + result_2
# print(result.numerator, result.denominator)

# a = 1987
# for i in range(a + 1, 10001):
#     if len(set(str(i))) == len(str(a)):
#         print(i)
#         break
# '''from collections import Counter

# a = [int(x) for x in '8 100 1'.split()]
# b = [x.isupper() for x in 'keepcalm']
# result = 0
# if Counter(b).most_common(1)[0][0] == False:
#     for x in b:
#         if x is True:
#             result += a[1]
# else:
#     for x in b:
#         if x is False:
#             result += a[2]
    
# print(result)'''

# a = int(input())
# list1 = []
# for i in range(a-1, 0, -1):
#     if a % i == 0:
#         list1.append(i)
# result = len(list1)
# max_val = list1[0]
# while max_val >= 1:
#     count = 0
#     max_val_tmp = []
#     for k in range(max_val-1, 0, -1):
#         if max_val % k == 0:
#             max_val_tmp.append(k)
#             count += 1
#     result += count
#     max_val = max_val_tmp[0]
# print(result)

# import sys
# a = [a.strip() for a in sys.stdin.readlines()][1:]
# health = []
# damage_from_each_gun = []
# x = 0
# k = 1
# while x < len(a):
#     health.append(a[x].replace(a[x][0], '', 1).strip())
#     x += 2
# while k < len(a):
#     damage_from_each_gun.append(a[k].split())
#     k += 2
# health = [int(x) for x in health]
# for x in damage_from_each_gun:
#     print(max(x))
# print(health)
# print(damage_from_each_gun)


# import sys

# a = [x.strip() for x in sys.stdin.readlines()][1:]
# print(a)
# for i in a:
#     if len(i) > 10:
#         print(f'{i[0]}{len(i[1:-1])}{i[-1]}')
#     else:
#         print(i)

# try:
#     print('0.'+input().split('.')[1])
# except IndexError:
#     print('0')

# x = float(input())
# print(x - int(x))

# print(input().split('.')[1][0])

# x = float(input())
# print(int(x * 10) % 10)

# import sys
# from itertools import permutations

# a = [x.strip() for x in sys.stdin.readlines()][1:]
# for i in a:

# for i in a:
#     list1 = ([x for x in range(int(i.split()[1])+1)])
#     print(list1)
#     print(permutations(list1))
#     # for k in range(int(i.split()[1])+1):
#     #     list1.append(k)
#     #     print(permutations(str(int(i[0])**list1[k])))


# from itertools import permutations
# a = 3
# for i in permutations(range(5)):
#     print(i)


# import sys

# a = [x.strip() for x in sys.stdin.readlines()][1:]
# for i in a:
#     j = i
#     for k in range(len(i)+1):
#         if i[k]:
#             continue
#         else:
#             j.replace(i[k], '0')
#     print(j)

# print(len([x for x in list(set(i)) if x != '0']))


# import sys

# a = [x.strip() for x in sys.stdin.readlines()][1:]
# for i in a:
#     n, k = [int(x) for x in i.split()]
#     print((k-1)/(n-1))


# import sys
# from collections import Counter

# a = [x.strip() for x in sys.stdin.readlines()][1:]
# for i in a:
#     list1 = []
#     for k in i.split():
#         if len(set(i.split())) == 1:
#             list1.append(str(int(k)+1))
#         elif Counter(min(i.split())) == 2:
#             if int(k) == max(i.split()):
#                 list1.append(str(int(k))+1)
#             else:
#                 list1.append(str((int(max(i.split())) - int(k))+1))
#         else:
#             if int(k) < int(max(i.split())):
#                 list1.append(str((int(max(i.split())) - int(k))+1))
#             else:
#                 list1.append('0')
#     print(' '.join(list1))


# a = [x.strip() for x in sys.stdin.readlines()][1:]
# print(a)
# for i in a:
#     list1 = [int(x) for x in i.split()]
#     print(list1)
#     a, b, c = list1
#     print(a,b,c)
#     maxval = max(a,b,c)
#     if len(set(list1)) == 1:
#         print(f'{a+1} {b+1} {c+1}')
#     else:
#         if a == maxval:
#             print(f'0 {(a-b)+1} {(a-c)+1}')
#         if b == maxval:
#             print(f'{(b-a)+1} 0 {(b-c)+1}')
#         if c == maxval:
#             print(f'{(c-a)+1} {(c-b)+1} 0')

    # list1 = [int(x) for x in i.split()]
    # maxval = max(list1)
    # if len(set(list1)) == 1:
    #     print(' '.join([str(i+1) for i in list1]))
    # else:
    #     if 


# import sys

# a = input(); b = input()
# print(''.join(sorted((b.replace('6', '9')).split(' '), reverse=True)))

# a = [x.strip() for x in sys.stdin.readlines()][1:]
# list1 = ['9' if k=='6' else k for k in [x for x in ''.join(a).split()]]
# print(''.join(sorted(list1, reverse=True)))

# import sys

# a = [x.strip() for x in sys.stdin.readlines()][1:]
# b = a[1::2]; c = a[::2]
# # print(c, b) # Example: ['2', '3', '4'] ['3 8', '15 16 1', '1 4 10 11']
# for k, i in enumerate(b): # first value is a counter
#     pass


# a = int(input())
# time = 540
# if a % 2 == 0:
#     # 15 min
#     time += (45*a)+15
# else:
#     # 5 min
#     time += (45*a)+5
# print(time // 60, time % 60)


# a = int(input())
# time = 540
# hour = 0
# mint = 0
# for i in range(1 ,a+1):
#     if i % 2 == 0:
#         time += 45
#         hour = time // 60
#         mint = time % 60
#     else:
#         time += 45 if i == 1 else 45 + 5
# print(time // 60, time % 60)


# a = int(input())
# # b = int(input())
# for i in range(a+1):
#     print('*' * i)


# a = int(input())
# time = 540
# if a % 2 == 0:
#     pass 
# else:
#     pass
# print()


# a = int(input()); b = int(input()); n = int(input())
# print(a*n + b*n // 100, b*n % 100)


# n, m = [int(x) for x in input().split()]
# count = 0
# while m > n:
#     if m % 2 == 0:
#         m /= 2
#     else:
#         m += 1
#     count += 1
# print(int(count + n - m))

# import sys


# a = [x.strip() for x in sys.stdin.readlines()]
# print(a)
# horses, bet, forecast = a[0].split()
# best = 0
# if int(horses) - int(forecast) >= 2:
#     print('No')
# else:
#     for i in a[1:]:
#         first, second = i.split()
#         best = first
#     if bet == best:
#         print('Yes')
#     else:
#         print('No')


# a = int(input())
# a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
# print(a // 60 + 9, a % 60)

# import random

# count = [0] * 10
# # print(count)
# for i in range(11):
#     numereal = random.randint(1, 10)
#     count[numereal - 1] += 1
# print(count)