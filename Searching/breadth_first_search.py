the_most_dangerous_graph = {
	'lava': {'sharks', 'piranhas'},
	'sharks': {'lava', 'bees', 'lasers'},
	'piranhas': {'lava', 'crocodiles'},
	'bees': {'sharks'},
	'lasers': {'sharks', 'crocodiles'},
	'crocodiles': {'piranhas', 'lasers'}
}


def bfs(graph, start_vertex, target_value):
	path = [start_vertex]
	vertex_and_path = [start_vertex, path]
	bfs_queue = [vertex_and_path]
	visited = set()

	while bfs_queue:
		current_vertex, path = bfs_queue.pop(0)
		visited.add(current_vertex)

		for neighbor in graph[current_vertex]:
			if neighbor not in visited:
				if neighbor == target_value:
					return path + [neighbor]
				else:
					bfs_queue.append([neighbor, path + [neighbor]])


print(bfs(the_most_dangerous_graph, "crocodiles", "bees"))

