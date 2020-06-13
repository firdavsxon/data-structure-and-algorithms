class EmtyStackError(Exception):
	pass

class Stack:
	def __init__(self):
		self.items =[]

	def is_empty(self):
		return self.items == []

	def size(self):
		print("Element size is: ", len(self.items))
		return len(self.items)

	def push(self, x):
		self.items.append(x)

	def pop(self):
		if self.is_empty():
			raise EmtyStackError("Stack is empty.")
		return self.items.pop()

	def peek(self):
		if self.is_empty():
			raise EmtyStackError("Stack is empty")
		return self.items[-1]

	def display(self):
		print(self.items)


