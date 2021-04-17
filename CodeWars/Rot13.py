'''My solution(helped)'''
def rot13(message):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in message:
        #lowercase
        if i in alpha:
            res += alpha[(alpha.index(i) + 13) % len(alpha)]
        #Uppercase
        elif i in alpha.upper():
            res += alpha.upper()[(alpha.upper().index(i)+ 13) % len(alpha)]
        #other symbols
        else: res += i
    return res

'''Most popular solution'''
'''
import string
from codecs import encode as _dont_use_this_
from string import maketrans, lowercase, uppercase

def rot13(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)
'''
