import numpy as np

N = 4
M = 6
L = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A = A + A[L]

print("Новая матрица: " + str(A))