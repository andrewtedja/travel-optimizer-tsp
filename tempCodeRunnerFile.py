    start = 0  # titik awal perjalanan

    # Dynamic Programming
    start_time = time.time()
    total_distance_dp, path_dp = dp_tsp(graph, start)
    end_time = time.time()
    runtime_dp = end_time - start_time
    print(color("\nTSP - Dynamic Programming", 94))
    print(f"Jarak total perjalanan: {(total_distance_dp)} km")
    print(f"\nJalur optimal (simpul): {' -> '.join(map(str, path_dp))}")

    path_with_names = [index_to_location[i] for i in path_dp]
    print(color(" -> ".join(path_with_names), 93))
    
    # Runtime DP
    print(color(f"Runtime: {end_time - start_time} detik", 92))
    print()

    # Brute Force
    start_time = time.time()
    total_distance_bf, path_bf = brute_force_tsp(graph, start)
    end_time = time.time()
    runtime_bf = end_time - start_time
    print(color("TSP - Brute Force", 94))
    print(f"Jarak total perjalanan: {total_distance_bf} km")
    print(f"\nJalur optimal (simpul): {' -> '.join(map(str, path_bf))}")
    path_with_names = [index_to_location[i] for i in path_bf]
    print(color(" -> ".join(path_with_names), 93))

    # Runtime BF
    print(color(f"Runtime: {end_time - start_time} detik", 91))
    print()

    print(f"Perbandingan runtime DP vs BF (approximately): {runtime_bf/runtime_dp:.2f} kali lebih cepat")