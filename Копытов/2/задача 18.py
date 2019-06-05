import numpy as np

N = 4
M = 6
L = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

diagonal_main = np.diagonal(A)
print("Элементы главной диагонали: "+ str(diagonal_main))

sum_diagonal_main = np.sum(diagonal_main)
print("Cумма элементов главной диагонали: "+ str(sum_diagonal_main))

diagonal_side = np.diagonal(A[::-1])
print("Элементы побочной диагонали: "+ str(diagonal_side))

sum_diagonal_side = np.sum(diagonal_side)
print("сумму элементов побочной диагонали: "+ str(sum_diagonal_side))