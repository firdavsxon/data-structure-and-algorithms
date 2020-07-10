numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 3, 8, 77, 0]
letter_list = ["paper", "true", "soap", "floppy", "flower"]
letters = ['d', 'e', 'q', 'x', 'er', 'a', 'ws', 'l', 'b', 'a']


def merge_sort(array):
	if len(array) == 1:
		return array
	# split array to left and right
	middle = len(array)//2
	left = array[:middle]
	right = array[middle:]
	sleft = merge_sort(left)
	sright = merge_sort(right)
	return merge(merge_sort(sleft), merge_sort(sright))


def merge(left, right):
	result = []
	while (left and right):
		if left[0] < right[0]:
			result.append(left[0])
			left.pop(0)
		else:
			result.append(right[0])
			right.pop(0)
	if left:
		result += left
	if right:
		result += right
	return result


print(f'Pre-order numbers: {numbers}')
print(f'Post-order numbers: {merge_sort(numbers)}')