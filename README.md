# TSP Travel Optimizer

> Tugas Makalah Matematika Diskrit 2024 - Andrew Tedjapratama 13523148

**TSP Travel Optimizer** adalah program Python untuk menyelesaikan masalah Travelling Salesman Problem (TSP) pada graf berbobot, dengan fokus pada rute optimal perjalanan wisata di kawasan Pegunungan Bandung. Program ini mengimplementasikan dua algoritma, yaitu **Dynamic Programming (DP)** dan membandingkannya dengan algoritma **Brute Force**, untuk menentukan jalur perjalanan terpendek dan mengevaluasi keunggulan efisiensi pendekatan **Dynamic Programming (DP)**

---

![TSP Travel Optimizer Visualization](public/TSP.png)

## Fitur

-   **Dynamic Programming**: Menggunakan algoritma Held-Karp untuk menyelesaikan TSP secara efisien pada dataset sedang hingga besar.
-   **Brute Force**: Mengevaluasi semua kemungkinan jalur untuk menemukan solusi optimal pada dataset kecil.
-   **Perbandingan Runtime**: Membandingkan kecepatan eksekusi kedua algoritma.
-   **Visualisasi Jalur**: Menyediakan output rute perjalanan optimal berdasarkan simpul dan nama lokasi wisata.

---

## Prerequisites

Pastikan Anda telah menginstall Python 3.6 atau versi lebih baru. Anda juga memerlukan beberapa pustaka berikut:

-   **NumPy**: Untuk operasi matematis pada matriks.
-   **itertools**: Library bawaan Python untuk menghasilkan permutasi.

Untuk menginstal NumPy, gunakan:

```bash
pip install numpy

```

## Cara penggunaan

```bash
git clone https://github.com/andrewtedja/tsp-travel-optimizer.git
cd tsp-travel-optimizer
```

```bash
python main.py
```
## Referensi

1. Munir, Rinaldi. (2024). “Graf: Bagian 1”.  
[https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2024-2025/20-Graf-Bagian1-2024.pdf](https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2024-2025/20-Graf-Bagian1-2024.pdf) (Accessed: 29 December 2024)

2. Ipython Books, "Graphs, Geometry, and Geographic Information Systems".  
   [https://ipython-books.github.io/chapter-14-graphs-geometry-and-geographic-information-systems/](https://ipython-books.github.io/chapter-14-graphs-geometry-and-geographic-information-systems/) (Accessed: 29 December 2024)

3. Munir, Rinaldi. (2024). “Graf: Bagian 2”.  
   [https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2024-2025/21-Graf-Bagian2-2024.pdf](https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2024-2025/21-Graf-Bagian2-2024.pdf) (Accessed: 29 December 2024)

4. Munir, Rinaldi. (2024). “Graf: Bagian 3”.  
   [https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2024-2025/22-Graf-Bagian3-2024.pdf](https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/2024-2025/22-Graf-Bagian3-2024.pdf) (Accessed: 29 December 2024)

5. GeeksforGeeks, "Travelling Salesman Problem using Dynamic Programming".  
   [https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/?ref=ml_lbp](https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/?ref=ml_lbp) (Accessed: 7 January 2025)

6. Andrew Tedjapratama, "travel-optimizer-tsp," GitHub repository.  
   [https://github.com/andrewtedja/travel-optimizer-tsp](https://github.com/andrewtedja/travel-optimizer-tsp) (Accessed: 8 January 2025)
