class EmptyQueueError(Exception):
	pass


class Node:
	def __init__(self, value):
		self.data = value
		self.next = None

class QueueLinked:

	def __init__(self):
		self.head = None
		self.tail = None
		self.list_size_queue = 0

	def is_empty(self):
		return self.head == None

	def enqueue(self, data):
		temp = Node(data)
		if self.is_empty():
			self.head = temp
		else:
			self.tail.next = temp
		self.tail = temp
		self.list_size_queue += 1

	def dequeue(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")
		x = self.head.data
		self.head = self.head.next
		self.list_size_queue -= 1
		return x

	def peek(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")
		print(self.head.data)
		return self.head.data

	def display(self):
		if self.is_empty():
			print("Display is empty")
			return
		print("Queue is : ")
		p = self.head
		while p is not None:
			print(p.data)
			p = p.next


