import numpy as np

def dp_tsp(graph, start):
    n = len(graph)
    graph = np.array(graph)
    memo = np.full((n, 1 << n), -1, dtype=float)
    parent = np.full((n, 1 << n), -1, dtype=int)

    def visit(mask, pos):
        if memo[pos, mask] != -1:
            return memo[pos, mask]

        if mask == (1 << n) - 1:
            return graph[pos, start]

        min_distance = float('inf')
        for city in range(n):
            if mask & (1 << city) == 0:
                distance = graph[pos, city] + visit(mask | (1 << city), city)
                if distance < min_distance:
                    min_distance = distance
                    parent[pos, mask] = city

        memo[pos, mask] = min_distance
        return min_distance

    total_distance = visit(1 << start, start)

    # Reconstruct path
    best_path = [start]
    mask = 1 << start
    pos = start
    while parent[pos, mask] != -1:
        next_pos = parent[pos, mask]
        best_path.append(next_pos)
        mask |= (1 << next_pos)
        pos = next_pos

    best_path.append(start)
    return total_distance, best_path
