import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A_bool = A < 0
num_cols = np.sum(A_bool, axis=0)
num_rows = np.sum(A_bool, axis=1)
A = np.vstack((A, [num_cols]))
A = np.column_stack((A, np.append(num_rows, 0)))

print("Новая матрица: " + str(A))