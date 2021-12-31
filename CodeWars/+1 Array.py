'''My solution'''
def up_array(arr):
    return [int(x) for x in str(int(''.join([str(x) for x in arr])) + 1)] if all(x != '' and x >= 0 and x < 10 for x in arr) and arr != [] else None


#Refactoring
def up_array(arr):
    return None if not arr or min(arr) < 0 or max(arr) > 9 else [int(x) for x in str(int(''.join([str(x) for x in arr])) + 1)]


print(up_array([2, 3, 9]))
print(up_array([1, -9]))
print(up_array([]))

'''Best practices'''
def up_array(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]


def up_array(arr):
    return None if arr==[] or any([x not in range(10) for x in arr]) else [int(c) for c in str(int("".join([str(x) for x in arr]))+1)]
