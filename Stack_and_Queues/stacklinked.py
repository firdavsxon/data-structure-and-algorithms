class EmptyStackError(Exception):
	pass


class Node:
	def __init__(self, value):
		self.data = value
		self.next = None


class StackLinked:

	def __init__(self):
		self.top = None

	def is_empty(self):
		return self.top == 0

	def size(self):
		if self.is_empty():
			return 0

		count =0
		p=self.top
		while p is not None:
			count += 1
			p=p.next
		return count

	def push(self, data):
		temp = Node(data)
		temp.next = self.top
		self.top = temp

	def pop(self):
		if self.is_empty():
			raise EmptyStackError("Stack is empty")
		popping_data = self.top.data
		self.top = self.top.next
		return popping_data

	def peek(self):
		if self.is_empty():
			raise EmptyStackError("Stack is empty")
		return self.top.data

	def display(self):
		if self.is_empty():
			print("Stack is empty")
			return
		print("Stack is: ")
		p = self.top
		while p is not None:
			print(p.data, " ")
			p = p.next