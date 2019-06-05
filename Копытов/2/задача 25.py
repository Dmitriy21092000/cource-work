import numpy as np

N = 4
M = 6
K = 2
L = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A_bool = A == 0
col = np.sum(A_bool, axis=1)
A = np.insert(A, M, col, axis=1)

row = np.append(np.sum(A_bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)

print("Новая матрица: " + str(A))