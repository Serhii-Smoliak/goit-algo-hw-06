from task_1.task_1 import create_graph


def dijkstra(graph, start):
	shortest_paths = {node: float('inf') for node in graph.nodes}
	shortest_paths[start] = 0
	queue = list(graph.nodes)

	while queue:
		current_node = min(queue, key=lambda node: shortest_paths[node])
		queue.remove(current_node)

		for neighbor in graph.neighbors(current_node):
			weight = graph[current_node][neighbor]['weight']
			new_path = shortest_paths[current_node] + weight
			if new_path < shortest_paths[neighbor]:
				shortest_paths[neighbor] = new_path

	return shortest_paths


if __name__ == "__main__":
	# Створюємо граф
	new_graph = create_graph()

	# Додаємо ваги до ребер
	for edge in new_graph.edges:
		new_graph.edges[edge]['weight'] = 1

	# Знаходимо найкоротший шлях від кожної вершини до всіх інших вершин
	for node in new_graph.nodes:
		shortest_paths = dijkstra(new_graph, node)
		print(f"Найкоротші шляхи від вершини {node}: {shortest_paths}")
