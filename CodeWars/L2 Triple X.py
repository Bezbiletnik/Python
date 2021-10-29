import re


def triple_x(s):
    return re.search(r'xxx', s)


print((triple_x('soft kitty, warm kitty, xxxxx'), True))
print((triple_x(""), False))
print((triple_x("there's no XXX) here"), False))
print((triple_x("abraxxxas"),True))
print((triple_x("xoxotrololololololoxxx"),False))
print((triple_x("soft kitty), warm kitty, xxxxx"),True))
print((triple_x("softx kitty, warm kitty, xxxxx"),False))