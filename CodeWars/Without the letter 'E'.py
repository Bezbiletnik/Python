from collections import Counter

def find_e(s):
    # return Counter(map(str.lower, s))['e']
    return '{}'.format(Counter(map(str.lower, s))['e']) if not 0 else 'There is no "e".'


print(find_e('actual'))
print(find_e('English'))