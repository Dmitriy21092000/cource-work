import numpy as np

N = 4
M = 6
K = 2

A = np.random.randint(0, 100, (N, M))
print("Матрица: " + str(A))

M_n = np.sum(A, axis=0) * (-1)

A = np.vstack((A, M_n))

print("Новая матрица: " + str(A))