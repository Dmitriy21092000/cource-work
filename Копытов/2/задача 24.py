import numpy as np

N = 4
M = 6
K = 2
L = 3

A = np.random.randint(-10, 10, (N, M))
print("Матрица:" + str(A))

parts = [
    A[:L, :K],
    A[:L, K:],
    A[L:, :K],
    A[L:, K:],]
for i in range(len(parts)):
    print("Cумма элементов" + str(i+1) + "части:" + str(np.sum(parts[i])))