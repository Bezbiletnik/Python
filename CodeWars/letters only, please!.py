'''My solution'''
import re

def remove_chars(s):
    return re.sub('[^a-z A-Z]', '', s)


'''Best practices'''
import re

def remove_chars(s):
    return re.sub(r'[^a-zA-Z ]', '', s)


def remove_chars(s):
    return "".join( c for c in s if c.isalpha() or c==" " )