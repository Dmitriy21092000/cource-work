import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, N))
print("Матрица:" + str(A))

a = np.diagonal(A, 1)
a_sum = a.sum()
print("Элементы которые выше главной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_sum))


b = np.diagonal(A, -1)
b_sum = b.sum()
print("Элементы которые ниже главной диагонали: \n" + str(b) + "\nИх сумма = " + str(a_sum))