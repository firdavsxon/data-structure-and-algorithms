class Node:

	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


class Tree:

	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root.value

	def insert(self, data):
		new_node = Node(data)
		if self.root is None:
			self.root = new_node
		else:
			current_node = self.root
			while True:
				if data > current_node.value:
				# left
					if current_node.right is None:
						current_node.right = new_node
						return
					current_node = current_node.right
				else:
					# right
					if current_node.left is None:
						current_node.left = new_node
						return
					current_node = current_node.left






	def lookup(self, value):
		if self.root is None:
			return False
		current_node = self.root
		while current_node:
			if current_node.value > value:
				current_node = current_node.left
			elif current_node.value < value:
				current_node = current_node.right
			elif current_node.value == value:
				return current_node
		return False
		# if self.root is not None:
		# 	current = self.root
		# 	while current:
		# 		if current.value > value:
		# 			if current.left is None:
		# 				return False
		# 			if current.value == value:
		# 				return current
		# 			current = current.left
		# 		elif current.value == value:
		# 			return current
		# 		else:
		# 			if current.right is None:
		# 				return False
		# 			if current.value == value:
		# 				return current
		# 			current = current.right
		# return False

	def remove(self, value):
		if self.root is None:
			return False
		current_node = self.root
		print(current_node.value)
		parent_node = None
		while current_node:
			if value < current_node.value:
				parent_node = current_node
				current_node = current_node.left
			elif value > current_node.value:
				parent_node = current_node
				current_node = current_node.right
			elif current_node.value == value:
				# we have a match

				# option1: no right child
				if current_node.right is None:
					if parent_node is None:
						self.root = current_node.left
					else:
						# if parent > current value, make current left child a child of parent
						if current_node.value < parent_node.value:
							parent_node.left = current_node.left

						# if parent < current value, make left child a right child of parent
						elif current_node.value > parent_node.value:
							parent_node.right = current_node.left

				# option2: Right child which doesn't have a left child
				elif current_node.right.left is None:
					if parent_node is None:
						self.root = current_node.left
					else:
						current_node.right.left = current_node.left

						# if parent> current, make right child of the left the parent
						if current_node.value < parent_node.value:
							parent_node.left = current_node.right

						# if parent< current, make right child a right of a parent
						elif current_node.value > parent_node.value:
							parent_node.right = current_node.right

				# option3: Right child that has a left child
				else:
					# find the Right child's left most child
					leftmost = current_node.right.left
					leftmost_parent = current_node.right
					while leftmost.left is not None:
						leftmost_parent = leftmost
						leftmost = leftmost.left

						# parent's left subtree is now leftmost's subtree
						leftmost_parent.left = leftmost.left
						leftmost.left = current_node.left
						leftmost.right = current_node.right

						if parent_node is None:
							self.root = leftmost
						else:
							if current_node.value < parent_node.value:
								parent_node.left = leftmost
							elif current_node.value > parent_node.value:
								parent_node.right = leftmost
				return True





	def printTree(self, node):
		if node:
			self.printTree(node.left)
			print(node.value)
			self.printTree(node.right)


new_tree = Tree()
new_tree.insert(9)
new_tree.insert(4)
new_tree.insert(6)
new_tree.insert(20)
new_tree.insert(170)
new_tree.insert(15)
new_tree.insert(1)


new_tree.printTree(new_tree.root)
new_tree.remove(170)
print(new_tree.lookup(170))





