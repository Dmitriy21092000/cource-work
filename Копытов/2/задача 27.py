import numpy as np

N = 4
M = 6
H = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A_bool = A == H
col_sum = np.sum(A_bool, axis=1)
print("Строки в которых встречается значение: "+ str(H))
print(np.argwhere(col_sum).flatten())

print("Строки в которых нет значения: "+ str(H))
print(np.argwhere(col_sum == 0).flatten())