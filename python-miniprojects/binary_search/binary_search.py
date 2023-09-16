


def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return -1


# list must be sorted
def binary_search(list, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, high)
    
if __name__ == '__main__':
    list = [1, 3, 5, 8, 9, 10, 11, 12, 15]
    target = 10
    print(naive_search(list, target))
    print(binary_search(list, target))