# arr = [1,2,3]
# print(arr[2:])
# print(arr[:2])
arr = [19, 10, 5, 5, 4]
pivot = 19

b=[x for x in arr[1:] if x <= pivot]
print(b)

# for x in arr[1:]: 
#     if x <= pivot:
#         print(x)