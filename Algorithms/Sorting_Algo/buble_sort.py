def bubble_sort(arr, n):
    """
    :param arr: unsorted array, which to be sorted
    :param n: length of the array
    :return: Sorted array
    time complexity: O(n^2)
    Note: This algo is not best for Large Data set, use Merge Sort or Quick Sort Instead
    """
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
        print('after iteration:', i)


if __name__ == '__main__':
    arr = [11, 10, 20, 15, 2, 5]
    n = len(arr)
    print('unsorted arr :', arr)
    bubble_sort(arr, n)
    print('sorted array: ', arr)
