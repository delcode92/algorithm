def bubble_sort(n):
    x = len(n)
    for i in range(x-1):
        for j in range(x-i-1):
            if n[j] > n[j+1]:
                # swap here
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp


numbers = [5, 3, 8, 2, 1, 9, 4]
bubble_sort(numbers)

print(numbers)
