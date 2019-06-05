import numpy as np

N = 4
M = 6
L = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

row = np.random.randint(-9, 10, M)
print("Строка для вставки: " + str(row))

A = np.insert(A, L, row, axis=0)
print("Новая матрица: " + str(A))