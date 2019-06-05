import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

sum_e = np.sum(A)
sum_c = np.sum(A, axis=0)
A = np.vstack((A, [sum_c/sum_e]))

print("Новая матрица: " + str(A))