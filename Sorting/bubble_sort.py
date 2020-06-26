numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubblesort(lst):
	length = len(lst)
	for i in range(length-1):
		for j in range(length-1):
			if lst[j] > lst[j+1]:
				# swap numbers
				temp = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = temp
	print(lst)
	return lst

bubblesort(numbers)