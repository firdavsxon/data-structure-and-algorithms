numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 3, 8, 77, 0]
letter_list = ["paper", "true", "soap", "floppy", "flower"]
letters = ['d', 'e', 'q', 'x', 'er', 'a', 'ws', 'l', 'b', 'a']


def merge_sort(array):
	if len(array) == 1:
		return array
	# split array to left and right
	middle = len(array)//2   # middle element index
	left = array[:middle]
	right = array[middle:]
	sleft = merge_sort(left)  # dividing left side with recursive call
	sright = merge_sort(right)   # dividing right side with recursive call
	return merge(merge_sort(sleft), merge_sort(sright))   # returning merged list of divided lists


def merge(left, right):
	result = []
	while (left and right):  # while left and right is exists
		if left[0] < right[0]:  # if firts element of left side is smaller from first element of right side
			result.append(left[0])  # adding element to result list
			left.pop(0)  # deleting added element from left side list
		else:
			result.append(right[0])  # same process for right side
			right.pop(0)
	if left:    # if left side list element still exists add elements to result list
		result += left
	if right:    # if right side list element still exists add elements to result list
		result += right
	return result   # return final sorted list


print(f'Pre-order numbers: {numbers}')
print(f'Post-order numbers: {merge_sort(numbers)}')