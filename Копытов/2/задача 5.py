import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

average_rows = np.average(A, axis=1)

average_cols = np.average(A, axis=0)

A = np.vstack((A, [average_cols]))

A = np.column_stack((A, np.append(average_rows, 0)))

print("Новая матрица: " + str(A))