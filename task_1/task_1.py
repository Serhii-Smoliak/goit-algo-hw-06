import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
	G = nx.Graph()

	G.add_nodes_from([1, 2, 3, 4, 5, 6])

	edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (4, 6)]
	G.add_edges_from(edges)

	plt.figure(figsize=(8, 6))
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1,
			font_size=15)
	plt.title("Соціальна мережа")
	plt.show()

	return G


if __name__ == "__main__":
	new_graph = create_graph()

	# Аналіз основних характеристик графу
	print("Кількість вершин у графі:", new_graph.number_of_nodes())
	print("Кількість ребер у графі:", new_graph.number_of_edges())
	print("Ступінь кожної вершини:", dict(new_graph.degree()))
