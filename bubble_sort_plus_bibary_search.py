def bubble_sort(n):
    l = len(n)

    for i in range(l-1):
        for j in range(l-i-1):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    return n

def binary_search(numbers, t):
    n = bubble_sort(numbers)
    # print(n)

    l = 0
    u=len(n) - 1

    while l<=u:
        mid = (l+u) // 2
        if t == n[mid]:
            return mid
           
        else:
            if n[mid] < t:
                l = mid + 1
            elif n[mid] > t:
                u = mid - 1

numbers = [5, 3, 8, 2, 1, 9, 4]
target = 1

x = binary_search(numbers, target);
print(x)