class EmptyQueueError(Exception):
	pass

class Node:

	def __init__(self, data, priority):
		self.data = data
		self.priority = priority
		self.next = None


class PriorityQueue:

	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head is None

	def enqueue(self, data, data_priority):
		temp = Node(data, data_priority)

		if self.is_empty() or data_priority<self.head.priority:
			temp.next = self.head
			self.head = temp
		else:
			p = self.head
			while p.next is not None and p.next.priority <= data_priority:
				p = p.next
			temp.next = p.next
			p.next = temp

	def dequeue(self):
		if self.is_empty():
			raise EmptyQueueError("Queue is empty")
		x = self.head.data
		self.head = self.head.next
		return x

	def display(self):
		if self.is_empty():
			print("Queue is empty")
			return
		p = self.head
		while p is not None:
			print(p.data, " ", p.priority)
			p=p.next
		return

	def size(self):
		n=0
		p=self.head
		while p is not None:
			n+=1
			p = p.next
		return n




