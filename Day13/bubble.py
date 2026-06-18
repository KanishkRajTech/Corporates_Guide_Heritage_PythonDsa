def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                print(f'Swapped: {arr}')
    return arr

# Test
arr = [5, 3, 8, 1, 2]
print('Sorted:', bubble_sort(arr))
