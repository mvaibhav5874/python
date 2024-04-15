def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index)
        quick_sort(arr, partition_index + 1, high)

# Helper function for quick sort
def sort(arr):
    quick_sort(arr, 0, len(arr) - 1)

# Example usage:
arr = [5, 3, 8, 4, 2, 7, 1, 6]
sort(arr)
print("Sorted array:", arr)