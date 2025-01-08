from itertools import permutations

def brute_force_tsp(graph, start):
    n = len(graph)
    nodes = list(range(n))
    nodes.remove(start)  

    min_distance = float('inf')
    best_path = []

    for perm in permutations(nodes):
        # Kalkulasi permutasi total jarak
        current_distance = graph[start][perm[0]]  # start dari simpul awal
        for i in range(len(perm) - 1):
            current_distance += graph[perm[i]][perm[i + 1]]  
        current_distance += graph[perm[-1]][start]  # balik ke simpul awal

        if current_distance < min_distance:
            min_distance = current_distance
            best_path = [start] + list(perm) + [start]

    return min_distance, best_path
