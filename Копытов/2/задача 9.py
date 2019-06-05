import numpy as np

N = 4
M = 6
K = 3
L = 2

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

A_slice = A[:L, :K]
print("Срез: "+str(A_slice))
slice_bool = A_slice == 0
zero_elements = slice_bool.sum()

print("Количество элементов: "+str(zero_elements))