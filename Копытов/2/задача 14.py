import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))


max = np.max(A)
A = A / max

print("Новая матрица: " + str(A))