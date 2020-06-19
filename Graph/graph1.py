class Graph:

	def __init__(self):
		self.number_of_nodes = 0
		self.adjacent_list = {}

	def add_vertex(self, vertex):
		self.adjacent_list[vertex] = []
		self.number_of_nodes += 1

	def add_edge(self, vertex1, vertex2):
		if vertex1 in self.adjacent_list and vertex2 in self.adjacent_list:
			self.adjacent_list[vertex1].append(vertex2)
			self.adjacent_list[vertex2].append(vertex1)

		# undirected graph

	def show_connections(self):
		all_vertices = self.adjacent_list.keys()
		for node in all_vertices:
			node_connections = self.adjacent_list[node]
			connections = ""
			for vertex in node_connections:
				connections += vertex + " "
			print(node+" --> " + connections)


my_graph = Graph()

my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')
my_graph.add_edge('0', '1')
my_graph.add_edge('1', '3')
my_graph.add_edge('1', '2')
my_graph.add_edge('2', '4')
my_graph.add_edge('3', '4')
my_graph.add_edge('0', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('5', '6')

my_graph.show_connections()

