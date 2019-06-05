import numpy as np

N = 4
M = 6
K = 2

A = np.random.randint(0, 100, (N, M))
print("Матрица: " + str(A))

M_n = np.sum(A, axis=1) * (-1)

A = np.hstack((A, M_n.reshape(-1, 1)))

print("Новая матрица: " + str(A))