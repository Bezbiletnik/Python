'''My solution'''
#shitcode, but mine
string = 'Hello'
items = list(string)
result = []
for i in range(len(items) - 1, -1, -1):
    result.append(items[i])
print(''.join(result))

'''Most popular solution.'''
#def solution(str):
#  return str[::-1]