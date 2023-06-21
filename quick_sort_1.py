def quicksort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[1]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

# Example usage:
numbers = [1, 7, 4, 1, 10, 9, -2]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
