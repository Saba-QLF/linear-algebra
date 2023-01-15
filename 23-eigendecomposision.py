import numpy as np

A = np.array([[4, 2], [-5, -3]])
lambdas, V = np.linalg.eig(A)
V_inv = np.linalg.inv(V)
Lambda = np.diag(lambdas)
# put our eigenvalues in diagonal of a diagonal matrix

print(A)
print(np.dot(V, np.dot(Lambda, V_inv)))
# A = V * Lambda * V_inv
