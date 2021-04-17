from random import randint
from time import time
from os import system
from tabulate import tabulate

n = 0


def enter():
    global n
    try:
        print("Сколько случайных чисел должна создать программа?")
        n = int(input("> "))
        if n < 5:
            system('cls||clear')
            print("Желательно ввести число больше 5, иначе анализ будет весьма неточным")
            enter()
    except:
        system('cls||clear')
        print("Ошибка ввода")
        enter()


def main():
    enter()
    start = time()
    count1 = count2 = count3 = count4 = count5 = \
    count6 = count7 = count8 = count9 = count10 = 0



    for i in range(n):
        numeral = randint(1, 10)
        if numeral == 1:
            count1 += 1

        elif numeral == 2:
            count2 += 1
        
        elif numeral == 3:
            count3 += 1
        
        elif numeral == 4:
            count4 += 1
        
        elif numeral == 5:
            count5 += 1
        
        elif numeral == 6:
            count6 += 1
        
        elif numeral == 7:
            count7 += 1
        
        elif numeral == 8:
            count8 += 1
        
        elif numeral == 9:
            count9 += 1
        
        elif numeral == 10:
            count10 += 1

    top = [count1, count2, count3, count4, count5,
            count6, count7, count8, count9, count10]

    end = time()

    results = [(i + 1, '%.2f' % (top[i]/n*100), top[i]) for i in range(10)]
    print(
        ' Всего было создано %d случайных чисел' % n,
        '\n Анализ выполнился за %.2f секунд' % (end - start)
    )
    print(tabulate(results, headers=['Number', 'Percent', 'Quantity']))

    input("\nНажмите Enter, чтобы повторить: ")
    system('cls||clear')
    main()

main()