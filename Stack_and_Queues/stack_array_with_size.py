class EmtyStackError(Exception):
	pass


class StackFullError(Exception):
	pass

class Stack1:
	def __init__(self, max_size=10):
		self.items =[None] * max_size
		self.count = 0

	def is_empty(self):
		return self.count == 0

	def size(self):
		return self.count

	def is_full(self):
		return self.count == len(self.items)

	def push(self, x):
		if self.is_full():
			raise StackFullError("Stack is full, can't push")

		self.items[self.count] = x
		self.count += 1

	def pop(self):
		if self.is_empty():
			raise EmtyStackError("Stack is empty, can't pop")

		x = self.items[self.count-1]
		self.items[self.count-1] = None
		self.count -= 1
		return x

	def peek(self):
		if self.is_empty():
			raise EmtyStackError("Stack is empty, cant peek")
		return self.items[self.count-1]

	def display(self):
		print(self.items)


