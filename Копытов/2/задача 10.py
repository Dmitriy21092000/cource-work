import numpy as np

N = 4
M = 6
K = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

a = A[:, K]
a = a.reshape(len(a), 1)
A = A * a

print("Новая матрица: " + str(A))