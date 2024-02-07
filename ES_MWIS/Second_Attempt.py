import itertools
import time
import random

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def generate_random_points(num_points):
    points = set()

    while len(points) < num_points:
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        points.add((x, y))

    return list(points)

def generate_random_graph(num_points):
    points = generate_random_points(num_points)

    graph = [[0] * num_points for _ in range(num_points)]
    weights = [random.randint(1, 10) for _ in range(num_points)]

    for i in range(num_points):
        for j in range(i + 1, num_points):
            if random.random() < 0.5 and distance(points[i], points[j]) > 5:
                graph[i][j] = 1
                graph[j][i] = 1

    return graph, weights, points

def find_maximum_weight_independent_set(graph, weights):
    n = len(graph)
    vertices = list(range(n))
    
    max_weight = 0
    max_set = []

    num_operations = 0
    num_solutions_tested = 0

    for r in range(1, n + 1):
        combinations = itertools.combinations(vertices, r)

        for subset in combinations:
            num_solutions_tested += 1

            is_independent = all(graph[i][j] == 0 for i in subset for j in subset if i != j)
            num_operations += len(subset)**2

            if is_independent:
                total_weight = sum(weights[v] for v in subset)

                if total_weight > max_weight:
                    max_weight = total_weight
                    max_set = list(subset)

    return max_set, max_weight, num_operations, num_solutions_tested

import time

# Open a file in append mode ('a' for appending)
with open('output.txt', 'a') as file:
    # Perform experiments for successively larger problem instances
    for size in range(4, 11):
        graph, weights, points = generate_random_graph(size)

        start_time = time.time()
        max_independent_set, max_weight, num_operations, num_solutions = find_maximum_weight_independent_set(graph, weights)
        end_time = time.time()
        execution_time = end_time - start_time

        # Redirect the output to the file instead of using print
        file.write(f"\nExperiment for {size} vertices:\n")
        file.write(f"Vertices: {points}\n")
        file.write(f"Maximum Weight Independent Set: {[points[i] for i in max_independent_set]}\n")
        file.write(f"Maximum Weight: {max_weight}\n")
        file.write(f"Execution Time: {execution_time} seconds\n")
        file.write(f"Number of Basic Operations: {num_operations}\n")
        file.write(f"Number of Solutions Tested: {num_solutions}\n")

# The file is automatically closed when you exit the 'with' block


