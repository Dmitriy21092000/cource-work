import numpy as np

N = 4
M = 6

A = np.random.randint(-10, 10, (N, N))
print("Матрица:" + str(A))

for i in range(1, N-1):
    b = (A[i+1, i-1] + A[i-1, i+1])/2
    A[i+1, i-1] = b
    A[i-1, i+1] = b

print("Новая матрица: " + str(A))