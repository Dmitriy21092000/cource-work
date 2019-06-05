import numpy as np

N = 4
M = 6
K = 2

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A = np.delete(A, K, axis=1)

print("Новая матрица: " + str(A))