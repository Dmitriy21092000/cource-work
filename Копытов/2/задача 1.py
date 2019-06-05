import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

sum = A.sum(axis=0)

i = sum.argmax(axis=0)

max = A.max(axis=0)

max = max[i]

print("Наибольший элемент: " + str(max))