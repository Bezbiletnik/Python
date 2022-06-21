def sum_all(end: int):
    result = 0
    for i in range(1, end+1):
        result += i
    return result

print(sum_all(10000000))
        
