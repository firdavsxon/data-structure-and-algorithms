class EmptyQueueError(Exception):
	pass


class QueueArrayFixed:
	def __init__(self, default_size=10):
		self.items = [None] * default_size
		self.front = 0
		self.count = 0

	def is_empty(self):
		return self.count == 0

	def size(self):                           # function to extend size of the array if array becomes full
		return self.count

	def enqueue(self, item):
		if self.count == len(self.items):
			self.resize(2*len(self.items))
		i = (self.front + self.count) % len(self.items)
		self.items[i] = item
		self.count += 1

	def dequeue(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")

		x = self.items[self.front]
		self.items[self.front] = None
		self.front = (self.front + 1) % len(self.items)
		self.count -= 1
		return x

	def peek(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")
		print("first in the queue is: ", self.items[self.front])
		return self.items[self.front]

	def display(self):
		print(self.items)

	def resize(self, newsize):
		old_list = self.items
		self.items = [None] * newsize
		i = self.front
		for j in range(self.count):
			self.items[j] = old_list[i]
			i = (1+i) % len(old_list)
		self.front = 0





