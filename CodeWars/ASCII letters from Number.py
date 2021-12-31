'''My solution'''


def convert(number):
    i, list1 = 0, []    
    while i < len(number):
        list1.append(int(number[i] + number[i+1]))
        i += 2
    return ''.join([chr(x) for x in list1])


print(convert('656667'))


'''Best practices'''
def convert(number):
    return ''.join(chr(int(number[a:a + 2])) for a in range(0, len(number), 2))