numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 3, 8, 77, 0]
letter_list = ["paper", "true", "soap", "floppy", "flower"]
letters = ['d', 'e', 'q', 'x', 'er', 'a', 'ws', 'l', 'b', 'a']


def insertionSort(lst):
	length = len(lst)
	for i in range(1, length):
		currentValue = lst[i]
		position = i
		while position > 0 and lst[position-1]> currentValue:
			lst[position] = lst[position-1]
			position = position - 1
		lst[position] = currentValue
	return lst

print(f'Pre-order numbers: {numbers}')
print(f'Post-order numbers: {insertionSort(numbers)}')