import numpy as np

A = np.array([[-1, 2], [3, -2], [5, 7]])

U, d, VT = np.linalg.svd(A)

print('Left singular vectors')
print(U)
print('Singular values')
print(d)
print('Right singular vectors')
print(VT)

print('d should be diagonal:')
d = np.diag(d)

print('D must have the same dimensions as A:')
D = np.concatenate((d, [[0, 0]]), axis=0)
print(D)

print('Now calculating our formula: A = U*D*VT')
Ap = np.dot(U, np.dot(D, VT))
print(Ap)