numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 3, 8, 77, 0]


def selectionSort(lst):
	length = len(lst)
	for i in range(length-1):
		minIndex = i
		for j in range(i+1, length):
			if lst[j] < lst[minIndex]:
				minIndex = j
			if i !=minIndex:
				lst[i], lst[minIndex] = lst[minIndex], lst[i]
	return lst

print(f'Pre-order numbers: {numbers}')
print(f'Post-order numbers: {selectionSort(numbers)}')