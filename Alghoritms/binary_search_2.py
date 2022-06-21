numbers = [i for i in range (1, 1000)]
item = 1001

def search(items, item):
    head, tail = 0, len(items) - 1
    while head <= tail:
        mid = (head + tail) // 2
        if items[mid] < item:
            head = mid + 1 
        elif items[mid] == item:
            return mid
        else:
            tail = mid - 1 
    print("There is no such an item!")
    return

search(numbers, item)

