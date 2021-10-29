def series_sum(n):
    series = 1
    d = 1/3
    if n >= 2:
        series = series + (d*(n-1))
    return '%.2f' %series