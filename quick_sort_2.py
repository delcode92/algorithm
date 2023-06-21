import time


# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def quickSort(array, low, high):
	print(array)
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)

start_time = time.time()
data = [74, 63, 21, 65, 65, -68, 78, -76, 3, 33, 23, -9, 96, 
37, -77, -22, -71, -69, -67, -31, -34, -66, -35, 39, -84, 38, 13, 72, 48, -67, -41, -95, -18, 77, 12, -70, 35, 94, -62, -19, -17, 73, -73, -64, -76, -21, 72, 92, 
-54, 20, -87, -38, -100, 71, 53, 49, 87, 32, 89, 65, 51, 83, -96, -5, -88, 61, -75, 76, 75, -37, -4, 67, -90, 90, -41, -98, -72, -76, 96, -27, 98, 9, 34, 49, 80, 
16, 34, 61, -77, 98, 94, -37, -33, 87, -27, 27, 99, -38, 20, -43, -15, -12, -46, -92, -53, -10, -10, 12, 15, -63, 8, -9, 85, 98, 98, 15, 25, -95, -15, 95, -46, 43, 63, 56, -49, 29, -29, 12, -88, -38, 79, 11, 75, 63, 
-28, 11, 36, -20, -18, -81, -90, -93, -31, 67, 23, 85, 81, -80, 27, -98, 58, -17, -56, 52, -35, 62, 1, -55, 
93, -97, 29, 89, 15, -69, -24, 77, -38, -35, -19, 62, 
-22, -18, -58, -18, -93, -9, 41, -69, 90, -68, -7, -77, -22, -67, 39, 96, -34, 5, -1, 39, 55, 49, -25, 19, 98, 1, 54, 68, 4, -73]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

print("--- %s seconds ---" % (time.time() - start_time))