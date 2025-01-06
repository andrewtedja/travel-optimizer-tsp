from bruteforce_tsp import brute_force_tsp
from dp_tsp import dp_tsp
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear_screen()
    # Matriks jarak antar lokasi wisata (10x10)
    graph = [
        [0, 12, 43, 67, 89, 105, 135, 149, 150, 122],
        [12, 0, 31, 56, 78, 90, 113, 128, 140, 125],
        [43, 31, 0, 25, 49, 62, 85, 101, 114, 99],
        [67, 56, 25, 0, 23, 37, 59, 74, 88, 82],
        [89, 78, 49, 23, 0, 15, 39, 54, 68, 61],
        [105, 90, 62, 37, 15, 0, 24, 39, 54, 47],
        [135, 113, 85, 59, 39, 24, 0, 15, 30, 23],
        [149, 128, 101, 74, 54, 39, 15, 0, 19, 12],
        [150, 140, 114, 88, 68, 54, 30, 19, 0, 11],
        [122, 125, 99, 82, 61, 47, 23, 12, 11, 0]
    ]

    start = 0  # titik awal perjalanan
    clear_screen()
    print("\033[97m╔══════════════════════════════════════════════════════════════════════════════════╗\033[0m")
    print("\033[97m║                        T S P  T R A V E L  O P T I M I Z E R                     ║\033[0m")
    print("\033[97m║          Optimalisasi Rute Penjelajahan Wisata Alam Pegunungan Bandung           ║\033[0m")
    print("\033[97m╚══════════════════════════════════════════════════════════════════════════════════╝\033[0m")

    # Dynamic Programming
    start_time = time.time()
    total_distance_dp, path_dp = dp_tsp(graph, start)
    end_time = time.time()
    runtime_dp = end_time - start_time
    print("\033[96m\nTSP - Dynamic Programming\033[0m")
    print(f"Jarak total perjalanan: {total_distance_dp} km")
    print(f"Jalur optimal: {' -> '.join(map(str, path_dp))}")
    print(f"\033[92mRuntime: {end_time - start_time} detik\033[0m")
    print()

    # Brute Force
    start_time = time.time()
    total_distance_bf, path_bf = brute_force_tsp(graph, start)
    end_time = time.time()
    runtime_bf = end_time - start_time
    print("\033[93mTSP - Brute Force\033[0m")
    print(f"Jarak total perjalanan: {total_distance_bf} km")
    print(f"Jalur optimal: {' -> '.join(map(str, path_bf))}")
    print(f"\033[91mRuntime: {end_time - start_time} detik\033[0m")
    print()

    print(f"Perbandingan runtime DP vs BF (approximately): {runtime_bf/runtime_dp:.2f} kali lebih cepat")
