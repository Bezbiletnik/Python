num_count = int(input())
arr, sum = [], 0
for i in input().split():
    number = int(i)
    arr.append(number)
    
index_count = int(input())
for i in input().split():
    index = int(i)
    sum += arr[index]

print(sum)
