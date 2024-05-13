from task_1.task_1 import create_graph


def dfs(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			new_paths = dfs(graph, node, end, path)
			for new_path in new_paths:
				paths.append(new_path)
	return paths


def bfs(graph, start, end):
	queue = [(start, [start])]
	while queue:
		(vertex, path) = queue.pop(0)
		for next_node in graph[vertex]:
			if next_node == end:
				yield path + [next_node]
			elif next_node not in path:
				queue.append((next_node, path + [next_node]))


new_graph = create_graph()

# Пошук шляху в глибину (DFS) та виведення результатів
dfs_paths = dfs(new_graph.adj, 1, 5)
print("\nDFS шляхи від вершини 1 до 5:", dfs_paths)

# Пошук шляху в ширину (BFS) та виведення результатів
bfs_paths = list(bfs(new_graph.adj, 1, 5))
print("BFS шляхи від вершини 1 до 5:", bfs_paths)
