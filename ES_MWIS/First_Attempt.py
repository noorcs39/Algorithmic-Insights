import itertools
import time

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
            num_operations += len(subset)**2  # Counting the number of basic operations

            if is_independent:
                total_weight = sum(weights[v] for v in subset)

                if total_weight > max_weight:
                    max_weight = total_weight
                    max_set = list(subset)

    return max_set, max_weight, num_operations, num_solutions_tested

# Function to generate a random graph for testing
def generate_random_graph(n):
    import random
    graph = [[0] * n for _ in range(n)]
    weights = [random.randint(1, 10) for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.5:
                graph[i][j] = 1
                graph[j][i] = 1

    return graph, weights

import time

# Open a file in append mode ('a' for appending)
with open('output.txt', 'a') as file:
    # Perform experiments for successively larger problem instances
    for size in range(4, 11):
        graph, weights = generate_random_graph(size)

        start_time = time.time()
        max_independent_set, max_weight, num_operations, num_solutions = find_maximum_weight_independent_set(graph, weights)
        end_time = time.time()
        execution_time = end_time - start_time

        # Redirect the standard output to the file for each experiment
        with open('output.txt', 'a') as file:
            print(f"\nExperiment for {size} vertices:", file=file)
            print("Maximum Weight Independent Set:", max_independent_set, file=file)
            print("Maximum Weight:", max_weight, file=file)
            print("Execution Time:", execution_time, "seconds", file=file)
            print("Number of Basic Operations:", num_operations, file=file)
            print("Number of Solutions Tested:", num_solutions, file=file)

# The file is automatically closed when you exit the 'with' block


