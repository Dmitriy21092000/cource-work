import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

sum = A.sum(axis=0)

i = sum.argmin(axis=0)

min = A.min(axis=0)

min = min[i]

print("Минимальный элемент: " + str(min))