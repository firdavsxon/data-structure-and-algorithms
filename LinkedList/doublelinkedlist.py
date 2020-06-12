class Node:
	def __init__(self, value):
		self.data = value
		self.prev = None
		self.next = None


class DoubleLinkedList:
	def __init__(self):
		self.head = None

	def display_list(self):
		if self.head is None:
			print("List is empty")
			return
		print("List is: ")
		p = self.head
		while p is not None:
			print(p.data, " ", end='')
			p = p.next
		print()

	def insert_in_begining(self, data):
		temp = Node(data)
		temp.next = self.head
		self.head.prev = temp
		self.head = temp

	def insert_in_empty_list(self, data):
		temp = Node(data)
		self.head = temp

	def insert_at_end(self, data):
		temp = Node(data)
		p = self.head
		while p.next is not None:
			p = p.next
		p.next = temp
		temp.prev = p

	def create_list(self):
		n = int(input("Enter the number of nodes: "))
		if n==0:
			return
		data = int(input("Enter the first element to be inserted: "))
		self.insert_in_empty_list(data)

		for i in range(n-1):
			data = int(input("Enter the next element to be inserted: "))
			self.insert_at_end(data)

	def insert_after(self, data, x):
		temp = Node(data)
		p = self.head
		while p is not None:
			if p.data == x:
				break
			p = p.next
		if p is None:
			print(x, " not present in list")
		else:
			temp.prev = p
			temp.next = p.next
			if p.next is not None:
				p.next.prev = temp # should not be done when p refers to last node
			p.next = temp

	def insert_before(self, data, x):
		if self.head is None:
			print("List is empty")
			return
		if self.head.data == x:
			temp = Node(data)
			temp.next = self.head
			self.head.prev = temp
			return
		p = self.head
		while p is not None:
			if p.data == x:
				break
			p = p.next
		if p is None:
			print(x, " not present in list")
		else:
			temp = Node(data)
			temp.prev = p.prev
			temp.next = p
			p.prev.next = temp
			p.prev = temp

	def delete_first_node(self):
		if self.head is None: # list is empty
			return
		if self.head.next is None:   # list has only one node
			self.head = None
			return
		self.head = self.head.next
		self.head.prev = None

	def delete_last_node(self):
		if self.head is None:   # list is empty
			return
		if self.head.next is None:  # list has only one node
			self.head = None
			return
		p = self.head
		while p.next is not None:
			p = p.next
		p.prev.next = None

	def delete_node(self, x):
		if self.head is None:
			return
		if self.head.next is None:
			if self.head.data == x:
				self.head = None
			else:
				print(x, " not found")
			return
		# deletion of first node
		if self.head.data ==x:
			self.head = self.head.next
			self.head.prev = None
			return

		p = self.head.next
		while p.next is not None:
			if p.data == x:
				break
			p = p.next

		if p.next is not None:  # Node to be deleted is in between
			p.prev.next = p.next
			p.next.prev = p.prev
		else:  # p prefers to last node
			if p.data == x:  # node to be deleted is last node
				p.prev.next = None
			else:
				print(x, " not found")

	def reverse_list(self):
		if self.head is None:
			return
		p1 = self.head
		p2 = p1.next
		p1.next = None
		p1.prev = p2
		while p2 is not None:
			p2.prev = p2.next
			p2.next = p1
			p1=p2
			p2 = p2.prev
		self.head = p1






