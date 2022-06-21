def average(x):
    return sum(x) / len(x)

def calculate_variance(average, x):
    return sum([(i - average) ** 2 for i in x]) / (len(x) - 1)

def calculate_sd(variance):
    return variance ** 0.5

l = 6, 12, 15, 24, 27, 30, 42, 48 # <class 'tuple'>
print(calculate_sd(calculate_variance(average(l), l)))
