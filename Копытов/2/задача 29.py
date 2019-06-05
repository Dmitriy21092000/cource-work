import numpy as np

N = 4
M = 6
K = 2

A = np.random.randint(0, 100, (N, M))
print("Матрица: " + str(A))

col = np.random.randint(-9, 10, N)
print("Столбец для вставки: " + str(col))

A = np.insert(A, K, col, axis=1)
print("Новая матрица: " + str(A))