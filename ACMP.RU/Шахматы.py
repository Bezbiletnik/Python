import re

with open('ACMP.RU\input.txt', 'r') as file:
    a = file.readline()
    try:
        re.search(r'^[A-H][1-8]-[A-H][1-8]$', a).group()
        point1, point2 = a.split('-')
        print(point1, point2)
    except: print('ERROR')