import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

average = np.average(A, axis=1)

max = np.max(average)

print("Наибольшее среднее значение: " + str(max))