import numpy as np

X = np.array([[4, 2], [-5, -3]])
det = np.linalg.det(X)
print(det)

N = np.array([[-4, 1], [-8, 2]])
det2 = np.linalg.det(N)
print(det2)

B = np.array([[1, 2, 4],
              [2, -1, 3],
              [0, 5, 1]])
det3 = np.linalg.det(B)
print(det3)