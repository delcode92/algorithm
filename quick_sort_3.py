import time

from random import randint

def quicksort(array):
    print(array)
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]
    # pivot = array[]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


start_time = time.time()
print(quicksort([74, 63, 21, 65, 65, -68, 78, -76, 3, 33, 23, -9, 96, 
37, -77, -22, -71, -69, -67, -31, -34, -66, -35, 39, -84, 38, 13, 72, 48, -67, -41, -95, -18, 77, 12, -70, 35, 94, -62, -19, -17, 73, -73, -64, -76, -21, 72, 92, 
-54, 20, -87, -38, -100, 71, 53, 49, 87, 32, 89, 65, 51, 83, -96, -5, -88, 61, -75, 76, 75, -37, -4, 67, -90, 90, -41, -98, -72, -76, 96, -27, 98, 9, 34, 49, 80, 
16, 34, 61, -77, 98, 94, -37, -33, 87, -27, 27, 99, -38, 20, -43, -15, -12, -46, -92, -53, -10, -10, 12, 15, -63, 8, -9, 85, 98, 98, 15, 25, -95, -15, 95, -46, 43, 63, 56, -49, 29, -29, 12, -88, -38, 79, 11, 75, 63, 
-28, 11, 36, -20, -18, -81, -90, -93, -31, 67, 23, 85, 81, -80, 27, -98, 58, -17, -56, 52, -35, 62, 1, -55, 
93, -97, 29, 89, 15, -69, -24, 77, -38, -35, -19, 62, 
-22, -18, -58, -18, -93, -9, 41, -69, 90, -68, -7, -77, -22, -67, 39, 96, -34, 5, -1, 39, 55, 49, -25, 19, 98, 1, 54, 68, 4, -73]))

print("--- %s seconds ---" % (time.time() - start_time))