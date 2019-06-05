import numpy as np

N = 4
M = 6
L = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A = np.delete(A, L, axis=0)

print("Новая матрица: " + str(A))