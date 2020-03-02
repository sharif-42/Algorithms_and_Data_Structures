def recursive_binary_search(alist, item):
    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recursive_binary_search(alist[:midpoint], item)
            else:
                return recursive_binary_search(alist[midpoint + 1:], item)


def binary_search(arr, key):
    beg = 0
    end = len(arr) - 1

    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] == key:
            return True
        if key < arr[mid]:
            end = mid - 1
        else:
            beg = mid + 1

    return False


if __name__ == '__main__':
    arr = [1, 2, 5, 10, 20, 50, 100, 200]
    key = 200
    if recursive_binary_search(arr, 1000):
        print('Found')
    else:
        print('Not found')
