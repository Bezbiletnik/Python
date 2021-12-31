import re

with open('ACMP.RU\input.txt', 'r') as file:
        a = file.read().splitlines()[1:]
        minTimemin = 24 * 60 + 1 # 1441
        for i in a:
            name = re.search(r'".+"', i).group()
            a, b = re.findall(r'\d+:\d+', i)
            h1, m1 = int(a.split(':')[0]) * 60, int(a.split(':')[1])
            h2, m2 = int(b.split(':')[0]) * 60, int(b.split(':')[1])
            time1, time2 = h1 + m1, h2 + m2 
            if time2 > time1: time_min = time2 - time1
            else: time_min = time2 - time1 + 24 * 60
            if time_min < minTimemin:
                minTimemin = time_min
                best = name

        print(f'The fastest train is {best}.')
        print(f'Its speed is {round(650 * 60/minTimemin)} km/h, approximately.')