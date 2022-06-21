# import re
a = input()
# a = re.sub("/[*].+/[*]", "", a)
count, trigger = 0, False
for i in range(len(a)):
    if a[i] == "/" and a[i+1] == "*":
        print("Detect")
        trigger = not trigger
        continue
    if trigger:
        continue
    if a[i].isdigit():
        count += 1
print(count)
