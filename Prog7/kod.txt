import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def gen_temp(n):
    A = lil_matrix((n ** 2, n ** 2))
    b = np.zeros(n ** 2)
    for i in range(n):
        for j in range(n):
            index = i * n + j
            A[index, index] = -4
            if i > 0:
                A[index, index - n] = 1
            if i < n - 1:
                A[index, index + n] = 1
            if j > 0:
                A[index, index - 1] = 1
            if j < n - 1:
                A[index, index + 1] = 1
            if i == 0:
                b[index] -= 150
            if i == n - 1:
                b[index] -= 100
            if j == 0:
                b[index] -= 200
            if j == n - 1:
                b[index] -= 50
    return A.tocsc(), b


n = 41
A, b = gen_temp(n)
T = spsolve(A, b).reshape((n, n))
plt.imshow(T, cmap='hot', origin='lower', vmin=50, vmax=200)
plt.colorbar()
plt.show()
