numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 3, 8, 77, 0]


def bubblesort(lst):
	length = len(lst)
	for i in range(length):
		for j in range(length-i-1):
			if lst[j] > lst[j+1]:
				# swap numbers
				lst[j], lst[j+1] = lst[j+1], lst[j]
	return lst


print(f'Pre-order numbers: {numbers}')
print(f'Post-order numbers: {bubblesort(numbers)}')




