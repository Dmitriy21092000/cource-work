import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, N))
print("Матрица:" + str(A))

iu = np.triu_indices(N, 1)
a = A[iu]
a = np.sum(np.array(a))
print("\nCумма элементов выше главной диагонали = " + str(a))


b = np.fliplr(A)[iu]
b = np.prod(np.array(b))
print("\nПроизведение элементов выше побочной диагонали = " + str(b))