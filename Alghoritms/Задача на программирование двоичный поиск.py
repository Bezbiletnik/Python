n, *A = map(int, input().split())
k, *b = map(int, input().split())


def BinarySearch(A, i):
    l, r = 0, len(A) - 1
    while l <= r:
        m = l + (r - l) // 2
        if A[m] == i: return m + 1
        elif A[m] > i: r = m - 1
        else: l = m + 1
    return - 1


for i in b:
    print(BinarySearch(A, i), end=' ')
