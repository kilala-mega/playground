def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        while arr[i-1] > key and i >= 1:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = key
    return arr

arr = [3,4,1,7]
print(insertionSort(arr))
