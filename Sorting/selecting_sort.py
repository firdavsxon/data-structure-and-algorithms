numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 3, 8, 77, 0]
letter_list = ["paper", "true", "soap", "floppy", "flower"]
letters = ['d', 'e', 'q', 'x', 'er', 'a', 'ws', 'l', 'b', 'a']


def selectionSort(lst):
	length = len(lst)
	for i in range(length-1):
		minIndex = i
		for j in range(i+1, length):
			if lst[j] < lst[minIndex]:
				minIndex = j
			if i != minIndex:
				lst[i], lst[minIndex] = lst[minIndex], lst[i]
	return lst

print(f'Pre-order numbers: {letters}')
print(f'Post-order numbers: {selectionSort(letters)}')