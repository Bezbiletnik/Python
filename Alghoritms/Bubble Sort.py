def bubble_sort(a):
    '''Sort list by "bubble sort" algorithm'''
    pass

def insert_sort(a):
    '''Sort list by "insert sort" algorithm'''
    pass

def choise_sort(a):
    '''Sort list by "choise sort" algorithm'''
    pass


def test_quadratic_sorting_alghorithms(sort_algorithm):
    print('Testing: ', sort_algorithm.__doc__)
    print('Testcase #1: ', end='')
    a, a_sorted = [4, 5, 1, 3, 2], [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print('OK' if a==a_sorted else 'FAIL')

    print('Testcase #2: ', end='')
    a, a_sorted = [0, 10, 0, 0, 0], [0, 0, 0, 0, 10]
    sort_algorithm(a)
    print('OK' if a==a_sorted else 'FAIL')

    print('Testcase #3: ', end='')
    a, a_sorted = [3, 3, 1, 2, 4], [1, 2, 3, 3, 4]
    sort_algorithm(a)
    print('OK' if a==a_sorted else 'FAIL')

    print('Testcase #4: ', end='')
    a, a_sorted = list(range(11, 21)) + list(range(11)), list(range(21))
    sort_algorithm(a)
    print('OK' if a==a_sorted else 'FAIL')

if __name__ == '__main__':
    test_quadratic_sorting_alghorithms(bubble_sort)
    test_quadratic_sorting_alghorithms(insert_sort)
    test_quadratic_sorting_alghorithms(choise_sort)