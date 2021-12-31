'''My solution'''
def find_it(seq):
    return set([x for x in seq if seq.count(x) % 2 != 0]).pop()


'''Best practices'''
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i


from collections import Counter
def find_it(l):
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]