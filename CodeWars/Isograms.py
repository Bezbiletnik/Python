string = 'Dermatoglyphics'


def is_isogram(string):
    if len(string) == len(set(string.lower())):
        return True
    else: return False


print(is_isogram(string))

'''
    Best practices:


    def is_isogram(string):
        return len(string) == len(set(string.lower()))


'''