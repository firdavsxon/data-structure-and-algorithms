class Node:

	def __init__(self, value):
		self.data = value
		self.next = None


class SingleLinkedList:

	def __init__(self):
		self.head = None

	def display_list(self):

		if self.head is None:
			print("List is empty")
			return
		else:
			print("List is: ")
			a = self.head
			while a is not None:
				print(a.data, " ", end='')
				a = a.next
			print()

	def insert_at_end(self, data):

		temp = Node(data)
		if self.head is None:
			self.head = temp
			return
		a = self.head
		while a.next is not None:
			a = a.next
		a.next = temp

	def bubble_sort_exdata(self):
		end = None

		while end != self.head.next:
			a = self.head
			while a.next != end:
				q = a.next
				if a.data > q.data:
					a.data, q.data = q.data, a.data
				a = a.next
			end = a

	def create_list(self):

		n = int(input("Enter the number of nodes: "))
		if n == 0:
			return
		for i in range(n):
			data = int(input("Enter the element to be inserted: "))
			self.insert_at_end(data)

	def merge1(self, list2):
		merge_list = SingleLinkedList()
		merge_list.head = self._merge1(self.head, list2.head)
		return merge_list

	def _merge1(selfself, a1, a2):
		if a1.data <= a2.data:
			headM = Node(a1.data)
			a1 = a1.next
		else:
			headM = Node(a2.data)
			a2 = a2.next
		aM = headM

		while a1 is not None and a2 is not None:
			if a1.data <= a2.data:
				aM.next = Node(a1.data)
				a1 = a1.next
			else:
				aM.next = Node(a2.data)
				a2 = a2.next
			aM = aM.next
		# if second list has finished adn elements left in first list
		while a1 is not None:
			aM.next = Node(a1.data)
			a1 = a1.next
			aM = aM.next
		# if first list has finished and elements left in second list
		while a2 is not None:
			aM.next = Node(a2.data)
			a2 = a2.next
			aM = aM.next
		return headM

	def merge2(self, list2):
		merge_list = SingleLinkedList()
		merge_list.head = self._merge2(self.head, list2.head)
		return merge_list

	def _merge2(selfself, a1, a2):
		if a1.data <= a2.data:
			headM = a1
			a1 = a1.next
		else:
			headM = a2
			a2 = a2.next

		aM = headM

		while a1 is not None and a2 is not None:
			if a1.data <= a2.data:
				aM.next = a1
				aM = aM.next
				a1 = a1.next
			else:
				aM.next = a2
				aM = aM.next
				a2 = a2.next

		if a1 is None:
			aM.next = a2
		else:
			aM.next = a1
		return headM


list1 = SingleLinkedList()
list2 = SingleLinkedList()

list1. create_list()
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()


def printing_list():
	print("First "); list1.display_list()
	print("Second  "); list2.display_list()
	print()

printing_list()

list3 = list1.merge1(list2)
print("Merged "); list3.display_list()
print()

printing_list()

list3 = list1.merge2(list2)
print("Merged "); list3.display_list()
print()
printing_list()




