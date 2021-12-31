s = 'Доход'


def isPalindrome(strn, i):
    if i == len(strn) // 2:
        return True
    if strn[i] != strn[:-1-i]:
        return False
    return isPalindrome(s, i+=1)


isPalindrome(s, 0)