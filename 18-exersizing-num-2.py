import numpy as np

# 1:
identity_m = np.array([[2/3, 1/3, 2/3], [-2/3, 2/3, 1/3], [1/3, 2/3, -2/3]])
is_orthogonal = True
for i in range(3):
    for j in range(i + 1, 3):
        if np.dot(identity_m[:, i], identity_m[:, j]) != 0:
            is_orthogonal = False
if is_orthogonal:
    print('The matrix is orthogonal.')

# 2:
is_unit_vector = True
for i in range(3):
    norm = np.linalg.norm(identity_m[:, i])
    if norm != 1:
        is_unit_vector = False
if is_unit_vector:
    print("All columns are unit vector.")
