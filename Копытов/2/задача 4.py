import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

Average = A.mean(axis=1)

index = Average.argmin(axis=0)

min = Average.min(axis=0)

print("Наименьшее значение среди средних значений: " + str(min))