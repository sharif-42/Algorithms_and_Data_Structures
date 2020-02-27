def bubble_sort(arr, n):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] >= arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            print(arr)
        print('after iteration:', i)


if __name__ == '__main__':
    arr = [11, 10, 20, 15, 2, 5]
    n = len(arr)
    print('unsorted arr :', arr)
    bubble_sort(arr, n)
    print('sorted array: ', arr)
