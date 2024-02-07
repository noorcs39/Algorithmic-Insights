import networkx as nx
import random
import matplotlib.pyplot as plt


# Generate a random graph with 10 vertices and random edges
num_vertices = 10
graph = nx.gnm_random_graph(num_vertices, random.randint(num_vertices, num_vertices * 2))

# Display the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, font_weight='bold')
plt.show()

# Find the maximal independent set using Networkx
independent_set = nx.maximal_independent_set(graph)

# Display the graph with nodes in the maximal independent set highlighted in yellow
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray')

# Highlight nodes in the maximal independent set in yellow
nx.draw_networkx_nodes(graph, pos, nodelist=independent_set, node_color='yellow')

# Add text at the top of the graph
plt.text(0.5, 1.05, f"Maximal Independent Set: {independent_set}", horizontalalignment='center', fontsize=12, transform=plt.gca().transAxes)

plt.show()

print("Maximal Independent Set:", independent_set)