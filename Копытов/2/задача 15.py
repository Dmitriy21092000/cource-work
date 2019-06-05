import numpy as np

N = 4
M = 6
H = 4

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A_bool = A == H
row_sum = np.sum(A_bool, axis=0)

print("Столбцы в которых встречается значение:" + str(H))
print(np.argwhere(row_sum).flatten())
print("Столбцы в которых нет значения:" + str(H))
print(np.argwhere(row_sum == 0).flatten())