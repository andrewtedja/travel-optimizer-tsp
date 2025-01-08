from bruteforce_tsp import brute_force_tsp
from dp_tsp import dp_tsp
import time
import os

def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_title():
    print(color("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════╗", 97))
    print(color("║                                 T S P  T R A V E L  O P T I M I Z E R                                    ║", 97))
    print(color("║                     Optimalisasi Rute Penjelajahan Wisata Alam Pegunungan Bandung                        ║", 97))
    print(color("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════╝", 97))

index_to_location = {
    0: "Tebing Keraton",
    1: "Kawah Putih Ciwidey",
    2: "Tangkuban Perahu",
    3: "Gunung Putri Lembang",
    4: "Taman Hutan Raya",
    5: "Gunung Manglayang",
    6: "Bukit Moko",
    7: "Curug Maribaya",
    8: "Kebun Teh Sukawana",
    9: "Gunung Patuha"
}

if __name__ == "__main__":
    clear_screen()
    show_title()

    # Matriks jarak antar lokasi wisata (10x10)
    graph = [
        [0, 65.0, 28.1, 17.6, 5.0, 54.0, 7.7, 14.1, 24.7, 64.3],
        [65.0, 0, 78.7, 61.8, 60.0, 82.9, 66.7, 60.4, 70.9, 1.0],
        [28.1, 78.7, 0, 14.7, 23.0, 82.2, 27.8, 14.8, 12.0, 76.8],
        [17.6, 61.8, 14.7, 0, 12.2, 71.4, 19.5, 8.3, 13.6, 66.9],
        [5.0, 60.0, 23.0, 12.2, 0, 48.9, 9.3, 9.0, 19.6, 59.0],
        [54.0, 82.9, 82.2, 71.4, 48.9, 0, 39.1, 54.6, 73.5, 82.1],
        [7.7, 66.7, 27.8, 19.5, 9.3, 39.1, 0, 16.3, 29.4, 65.9],
        [14.1, 60.4, 14.8, 8.3, 9.0, 54.6, 16.3, 0, 15.9, 65.0],
        [24.7, 70.9, 12.0, 13.6, 19.6, 73.5, 29.4, 15.9, 0, 62.6],
        [64.3, 1.0, 76.8, 66.9, 59.0, 82.1, 65.9, 65.0, 62.6, 0]
    ]

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

