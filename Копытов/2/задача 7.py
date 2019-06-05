import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

sum_elements = np.sum(A)
sum_cols = np.sum(A, axis=1)
A = np.column_stack((A, sum_cols/sum_elements))

print("Новая матрица: " + str(A))