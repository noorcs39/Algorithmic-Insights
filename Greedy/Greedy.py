import itertools
import time
import random
import matplotlib.pyplot as plt
import networkx as nx
import sys

# Set the seed for randomness using your student number
random.seed(11799)

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def generate_random_points(num_points):
    points = set()

    while len(points) < num_points:
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        points.add((x, y))

    return list(points)

def calculate_max_edges(num_points):
    return int(0.75 * num_points * (num_points - 1))

def generate_random_graph(num_points, percentage):
    points = generate_random_points(num_points)

    max_edges = calculate_max_edges(num_points)
    target_edges = int(percentage * max_edges)

    graph = [[0] * num_points for _ in range(num_points)]
    weights = [random.randint(1, 10) for _ in range(num_points)]

    edges_added = 0

    while edges_added < target_edges:
        i, j = random.sample(range(num_points), 2)
        if graph[i][j] == 0 and distance(points[i], points[j]) > 5:
            graph[i][j] = 1
            graph[j][i] = 1
            edges_added += 1

    return graph, weights, points

def find_maximum_weight_independent_set_greedy(graph, weights):
    n = len(graph)
    vertices = list(range(n))
    
    # Sort vertices by weight in descending order
    sorted_vertices = sorted(vertices, key=lambda v: weights[v], reverse=True)

    independent_set = set()

    num_operations = 0
    num_solutions_tested = 0

    for vertex in sorted_vertices:
        # Check if the vertex is independent (not adjacent to any vertex in the independent set)
        if all(graph[vertex][v] == 0 for v in independent_set):
            independent_set.add(vertex)

        # Count basic operations and solutions tested
        num_operations += len(independent_set)**2
        num_solutions_tested += 1

    max_weight = sum(weights[v] for v in independent_set)

    return list(independent_set), max_weight, num_operations, num_solutions_tested

def visualize_graph(graph, points, max_independent_set):
    G = nx.Graph()

    for i in range(len(graph)):
        G.add_node(i, pos=points[i])

    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.get_node_attributes(G, 'pos')

    # Choose a different layout (e.g., circular layout)
    layout = nx.circular_layout(G)

    nx.draw(G, pos=layout, with_labels=True, font_weight='bold', node_size=700, node_color='gray')

    nx.draw_networkx_nodes(G, pos=layout, nodelist=max_independent_set, node_color='lightgreen', node_size=700)

    # Add a bounding box
    x_values, y_values = zip(*layout.values())
    plt.xlim(min(x_values) - 0.5, max(x_values) + 0.5)
    plt.ylim(min(y_values) - 0.5, max(y_values) + 0.5)

    plt.show()

# Open a text file in write mode
with open('output6.txt', 'w') as file:
    # Redirect standard output to the file
    sys.stdout = file

    # Perform experiments for successively larger problem instances
    percentages = [0.125, 0.25, 0.5]

    for size in range(4, 11):
        for percentage in percentages:
            graph, weights, points = generate_random_graph(size, percentage)

            start_time = time.time()
            max_independent_set, max_weight, num_operations, num_solutions = find_maximum_weight_independent_set_greedy(graph, weights)
            end_time = time.time()
            execution_time = end_time - start_time

            print(f"\nExperiment for {size} vertices and {percentage * 100}% of edges:")
            print("Vertices:", points)
            print("Maximum Weight Independent Set:", max_independent_set)
            print("Maximum Weight:", max_weight)
            print("Execution Time:", execution_time, "seconds")
            print("Number of Basic Operations:", num_operations)
            print("Number of Solutions Tested:", num_solutions)

            # Visualize the graph and solution
            visualize_graph(graph, points, max_independent_set)

    # Reset standard output to the console
    sys.stdout = sys.__stdout__
