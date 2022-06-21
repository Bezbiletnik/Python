n = int(input())
last_num, last_color = 0, 0
incorrect = 0
for i in range(n):
    inputs = input().split()
    num = int(inputs[0])
    color = inputs[1]
    if last_num != num and last_color != color:
        incorrect += 1
    last_num, last_color = num, color
    
print(incorrect)
