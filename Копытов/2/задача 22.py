import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

a = [i % 2 for i in np.sum(A, axis=1)]
A = np.insert(A, M, a, axis=1)

print("Новая матрица: " + str(A))