'''My solution'''

import re

def uncollapse(digits):
     return ' '.join(x for x in re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine)', digits))

    #I forgot that it's already a list


#Refactoring
import re

def uncollapse(digits):
    return ' '.join(re.findall('zero|one|two|three|four|five|six|seven|eight|nine', digits))


'''Best practices'''
import re

def uncollapse(digits):
    return ' '.join(re.findall('zero|one|two|three|four|five|six|seven|eight|nine', digits))