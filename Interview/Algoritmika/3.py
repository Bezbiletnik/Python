# Team lead said that it's not optimal solution
# First solution
def sum_chr(a: int):
    if a < 0:
        return 'Enter the valid number!'
    return sum([int(x) for x in str(a)])


print(sum_chr(456))