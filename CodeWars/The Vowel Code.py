'''My solution'''
def encode(st):
    return st.translate(st.maketrans('aeiou', '12345'))
    
def decode(st):
    return st.translate(st.maketrans('12345', 'aeiou'))

print(encode('hello'))
print(decode('h2ll4'))


'''Best practices'''
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)