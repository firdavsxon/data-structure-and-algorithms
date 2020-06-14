class EmptyQueueError(Exception):
	pass


class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


class QueueCircularLinked:

	def __init__(self):
		self.tail = None

	def is_empty(self):
		return self.tail is None

	def size(self):
		if self.is_empty():
			print("Queue is empty")
			return 0
		n = 1
		p = self.tail.next
		while True:
			n += 1
			p = p.next
			if p==self.tail:
				break
		return n

	def enqueue(self, data):
		temp = Node(data)
		if self.is_empty():
			self.tail = temp
			self.tail.next = self.tail
		else:
			temp.next = self.tail.next
			self.tail.next = temp
			self.tail = temp

	def peek(self):
		if self.is_empty():
			print("Queue is empty")
			return
		print("First element in the queue is ", self.tail.next.data )
		return self.tail.next.data

	def dequeue(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")
		if self.tail.next == self.tail:    #list has only one node
			x = self.tail
			self.tail = None
		else:
			x = self.tail.next
			self.tail.next = self.tail.next.next
		return x.data

	def display(self):
		if self.is_empty():
			print("Queue is empty")
			return
		p = self.tail.next
		while True:
			print(p.data)
			p=p.next
			if p == self.tail.next:
				break
		print()



