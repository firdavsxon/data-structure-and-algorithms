class HeapEmptyError(Exception):
	pass

class Heap:

	def __init__(self, maxsize=10):
		self.a = [None] * maxsize
		self.n = 0
		self.a[0] = 99999

	def insert(self, value):
		self.n += 1
		self.a[self.n] = value
		self.restore_up(self.n)

	def restore_up(self, i):  # i here is index
		k = self.a[i]
		iparent = i //2

		while self.a[iparent] < k: # No sential  - while(iparent >= 1 && self.a[iparent]<k)
			self.a[i] = self.a[iparent]
			i = iparent
			iparent = i // 2
		self.a[i] = k

	def delete_root(self):
		if self.n == 0:
			raise HeapEmptyError("Heap is empty")
		max_value = self.a[1]
		self.a[1] = self.a[self.n]
		self.n -= 1
		self.restore_down(1)
		return max_value

	def restore_down(self, i):
		k = self.a[i]
		left_child = 2*i
		right_child = left_child + 1

		while right_child <= self.n:
			if k > self.a[left_child] and k >= self.a[right_child]:
				self.a[i] = k
				return
			else:
				if self.a[left_child] > self.a[right_child]:
					self.a[i] = self.a[left_child]
					i = left_child
				else:
					self.a[i] = self.a[right_child]
					i = right_child

			left_child = 2*i
			right_child = left_child + 1

		# if number of nodes is even
		if left_child == self.n and k < self.a[left_child]:
			self.a[i]= self.a[left_child]
			i = left_child
		self.a[i] = k

	def display(self):
		if self.n == 0:
			print("Heap is empty")
			return
		print("Heap size is = ", self.n)
		for i in range(1, self.n +1):
			print(self.a[i], " ", end = ' ')
		print()


h = Heap(20)
while True:
	print("1. Isert")
	print("2. Delete root")
	print("3. Display")
	print(("4. Exit"))
	print("Enter your choice: ")
	choice = int(input("Enter your choice: "))

	if choice == 1:
		value = int(input("Enter the value to be inserted: "))
		h.insert(value)
	elif choice == 2:
		print("Maximum value is ", h.delete_root())
	elif choice == 3:
		h.display()
	elif choice == 4:
		break
	else:
		print("Wrong choice!")







