def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        curr = i
        for j in range(i+1, n):
            if arr[j] < arr[curr]:
                curr = j
        if i != curr:
            arr[i], arr[curr] = arr[curr], arr[i]
            
    return arr

arr = [3,4,1,7]
print(selectionSort(arr))
arr = [1]
print(selectionSort(arr))
arr = []
print(selectionSort(arr))
arr = [9,6,7]
print(selectionSort(arr))
