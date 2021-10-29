'''My solution'''
import re

def valid_number(n):
    try:
        bool(re.search(r'^[+-]?(\d+)?\.\d{2}$', n).group(0))
        return True
    except AttributeError:
        return False


#Refactoring
import re

def valid_number(n):
    return bool(re.fullmatch(r'^[+-]?(\d+)?\.\d{2}$', n))


'''Best Practices'''
import re
 

def valid_number(n):
    return bool(re.fullmatch(r'^[-+]?\d*\.\d{2}$', n))


import re

def valid_number(input_str):
    return re.match(r"""
        [+-]?   # optional +/- sign
        \d*     # optional digits
        \.      # decimal point
        \d\d    # two digits
        $       # end of string
        """, input_str, re.VERBOSE) is not None
