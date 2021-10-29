import re
strng = 'foobar099'
new_strng = re.search(r'\D+', strng).group(0)
length_1 = re.search(r'[0-9]+', strng).group(0)
length_2 = len(re.search(r'\d+', strng).group(0))
result = int(length_1) + 1
print(length_2)
print(new_strng)
result_2 = '{:0{}}'.format(result, length_2)
print(f'{new_strng}{result_2}')

