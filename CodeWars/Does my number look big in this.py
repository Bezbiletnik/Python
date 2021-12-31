def narcissistic(value):
    list1 = [int(x) ** len(str(value)) for x in str(value)]
    print(list1)

# narcissistic(153)