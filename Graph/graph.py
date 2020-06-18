# # edge list
# graph = [[0, 2], [2, 3], [3, 1], [1, 2]]
#
# # adjuceny list
# graph1 = [[2], [2, 3], [0, 1, 3], [1, 2]]
#
# # adjaceny matrix
# graph2 = {
# 	1: [0, 0, 1, 0],
# 	2: [0, 0, 1, 1],
# 	3: [1, 1, 0, 1],
# 	4: [0, 1, 1, 0]
# }


class Graph(object):
	def __init__(self, graph_dict=None):
		"""Initializes a graph object
		if no dictionary or None is given,
		an empty dictionary will be used """
		self.counting_nodes = 0
		if graph_dict is None:
			graph_dict = {}
		self._graph_dict = graph_dict

	def vertices(self):
		"""returns vertices of graph"""
		return list(self._graph_dict.keys())

	def edges(self):
		""" returns the edges f graph """
		return self._generate_edges()

	def add_vertex(self, vertex):
		"""if vertex "vertex" is not in
		self._graph_dict, a key "vertex" with an empty
		list as a value as added to the dictionary. Otherwise
		nothing has ti be done."""
		if vertex not in self._graph_dict:
			self._graph_dict[vertex] = []
			self.counting_nodes += 1

	def add_edges(self, edge):
		"""assumes that edge is type of set, tuple or list;
		netween two vetticies can be multiple edges!"""
		edge = set(edge)
		(vertex1, vertex2) =tuple(edge)
		if vertex1 in self._graph_dict:
			self._graph_dict[vertex1].append(vertex2)
		else:
			self._graph_dict[vertex1] = [vertex2]

	def _generate_edges(self):
		""" A static method generating the edges of the
		graph  "graph". Edges are represented as sets
		with one  (a loop back to the vertex) or two
		vertices
		"""
		edges = []
		for vertex in self._graph_dict:
			for neighbour in self._graph_dict[vertex]:
				if (neighbour, vertex) not in edges:
					edges.append({vertex, neighbour})
		return edges

	def __str__(self):
		res = "vertices: "
		for k in self._graph_dict:
			res += str(k) + " "
		res += "\nedges: "
		for edge in self._generate_edges():
			res += str(edge) + " "
		return res


if __name__ == "__main__":
	g = {
		"a": ["d"],
		"b": ["c"]
	}

graph = Graph(g)
print("Vertices of graph: ")
print(graph.vertices())

print("Edges of graph: ")
print(graph.edges())

print("Add vertex: ")
graph.add_vertex("d")

print("Vertices of graph: ")
print(graph.vertices())

print("Edges of graph: ")
print(graph.edges())

print('Adding an edge {"x","y"} with new vertices:')
graph.add_edges({"x", "y"})
print("Vertices of graph:")
print(graph.vertices())
print("Edges of graph:")
print(graph.edges())






