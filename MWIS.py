import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices, edges, weights):
        self.vertices = set(vertices)
        self.edges = edges
        self.weights = weights

def find_max_weighted_independent_set(graph):
    max_weighted_independent_set = set()

    # Sort vertices based on weights in descending order
    sorted_vertices = sorted(graph.vertices, key=lambda v: graph.weights[v], reverse=True)

    for vertex in sorted_vertices:
        if is_independent(vertex, max_weighted_independent_set, graph):
            max_weighted_independent_set.add(vertex)

    return max_weighted_independent_set

def is_independent(vertex, independent_set, graph):
    for v in independent_set:
        if (vertex, v) in graph.edges or (v, vertex) in graph.edges:
            return False
    return True

# Example usage
vertices = [1, 2, 3, 4, 5, 6, 7, 8]
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 8), (7, 8), (1, 8), (4, 5)]
weights = {1: 2, 2: 3, 3: 4, 4: 1, 5: 2, 6: 3, 7: 2, 8: 4}

graph = Graph(vertices, edges, weights)

# Original Graph
G = nx.Graph()
G.add_edges_from(graph.edges)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title('Original Graph')
plt.show()

# Maximum Weighted Independent Set (MWIS) Graph
mwis = find_max_weighted_independent_set(graph)
mwis_graph = G.subgraph(mwis)

nx.draw(mwis_graph, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=8, font_color='black', font_weight='bold')
edge_labels_mwis = nx.get_edge_attributes(mwis_graph, 'weight')
nx.draw_networkx_edge_labels(mwis_graph, pos, edge_labels=edge_labels_mwis, font_color='red')
print(mwis)
plt.title('Maximum Weighted Independent Set (MWIS) Graph')
plt.show()
