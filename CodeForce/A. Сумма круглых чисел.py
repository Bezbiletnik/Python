import sys

a = [x.strip() for x in sys.stdin.readlines()][1:]
print(a)
for i in a:
    for k in range(len(i)+1):
        if i[k] != 0:
            print(i[k])