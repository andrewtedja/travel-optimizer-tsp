import numpy as np
import time

def tsp(graph, start):
    n = len(graph)
    graph = np.array(graph)
    memo = np.full((n, 1 << n), -1, dtype=float)
    parent = np.full((n, 1 << n), -1, dtype=int)

    def visit(mask, pos):
        if memo[pos, mask] != -1:
            return memo[pos, mask]

        if mask == (1 << n) - 1:
            return graph[pos, start]

        min_cost = float('inf')
        for city in range(n):
            if mask & (1 << city) == 0:
                cost = graph[pos, city] + visit(mask | (1 << city), city)
                if cost < min_cost:
                    min_cost = cost
                    parent[pos, mask] = city

        memo[pos, mask] = min_cost
        return min_cost

    total_distance = visit(1 << start, start)

    # Reconstruct path
    path = [start]
    mask = 1 << start
    pos = start
    while parent[pos, mask] != -1:
        next_pos = parent[pos, mask]
        path.append(next_pos)
        mask |= (1 << next_pos)
        pos = next_pos

    path.append(start)
    return total_distance, path

if __name__ == "__main__":
    # Matriks jarak (10x10)
    graph = [
        [0, 568, 1234, 893, 431, 762, 1456, 897, 321, 1345, 432, 654, 1321, 675, 876],
        [568, 0, 643, 987, 432, 765, 897, 876, 567, 1456, 431, 876, 654, 987, 432],
        [1234, 643, 0, 789, 345, 567, 876, 543, 1321, 876, 765, 897, 876, 432, 231],
        [893, 987, 789, 0, 654, 1321, 543, 876, 765, 897, 432, 231, 876, 567, 987],
        [431, 432, 345, 654, 0, 876, 1234, 987, 567, 876, 765, 543, 678, 1321, 432],
        [762, 765, 567, 1321, 876, 0, 432, 897, 765, 567, 876, 876, 1321, 897, 654],
        [1456, 897, 876, 543, 1234, 432, 0, 765, 987, 876, 543, 432, 765, 654, 231],
        [897, 876, 543, 876, 987, 897, 765, 0, 432, 876, 987, 654, 876, 1234, 543],
        [321, 567, 1321, 765, 567, 765, 987, 432, 0, 678, 543, 1234, 987, 432, 876],
        [1345, 1456, 876, 897, 876, 567, 876, 876, 678, 0, 765, 543, 1321, 876, 543],
        [432, 431, 765, 432, 765, 876, 543, 987, 543, 765, 0, 1234, 678, 432, 897],
        [654, 876, 897, 231, 543, 876, 432, 654, 1234, 543, 1234, 0, 765, 987, 876],
        [1321, 654, 876, 876, 678, 1321, 765, 876, 987, 1321, 678, 765, 0, 543, 876],
        [675, 987, 432, 567, 1321, 897, 654, 1234, 432, 876, 432, 987, 543, 0, 321],
        [876, 432, 231, 987, 432, 654, 231, 543, 876, 543, 897, 876, 876, 321, 0]
    ]

    start = 0  # Titik awal perjalanan

    total_distance, path = tsp(graph, start)

    # Output
    print("Jarak total perjalanan:", total_distance, "meter")
    print("Jalur optimal:", " -> ".join(map(str, path)))

    # Test Runtime
    start_time = time.time()
    total_distance, path = tsp(graph, start)
    end_time = time.time()
    print("Runtime:", end_time - start_time, "detik")