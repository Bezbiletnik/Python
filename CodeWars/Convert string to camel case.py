'''My solution'''

import re

def to_camel_case(text):
    return re.split('-|_', text)[0] + ''.join([x.capitalize() for x in re.split('-|_', text)[1:]])


'''Best practices'''
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s


import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)