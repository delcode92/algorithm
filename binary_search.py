numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10


l = 0
u = len(numbers) - 1

while l<=u:
    mid = (l+u) // 2
    if target == numbers[mid]:
        print(mid)
        break
    else:
        if numbers[mid] < target:
            l = mid + 1
        elif numbers[mid] > target:
            u = mid - 1