class EmptyQueueError(Exception):
	pass


class QueueArray:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def size(self):
		print("Size of the queue: ", len(self.items))
		return len(self.items)

	def enqueue(self, item):
		self.items.append((item))

	def dequeue(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")
		return self.items.pop(0)

	def peek(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")
		print("first in the queue is: ", self.items[0])
		return self.items[0]

	def display(self):
		print(self.items)




