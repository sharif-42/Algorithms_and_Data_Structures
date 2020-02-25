def recursive_binary_search(alist, item):
    if len(alist) == 0:
        return False, None

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True, nums.index(item)
        else:
            if item < alist[midpoint]:
                return recursive_binary_search(alist[:midpoint], item)
            else:
                return recursive_binary_search(alist[midpoint + 1:], item)



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_found, index = recursive_binary_search(alist=nums, item=10)
    print(is_found, index)
