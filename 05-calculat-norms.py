import numpy as np
x = np.array([25, 2, 5])

# L2 NORM

# first method (you can try with for loop or anything else)
norm2 = (25**2 + 2**2 + 5**2) ** (1/2)
print(norm2)

# second method
norm2 = np.linalg.norm(x)
print(norm2)

# L1 NORM
norm1 = np.abs(25) + np.abs(2) + np.abs(5)
print(norm1)

# SQUARED L2 NORM
s_norm = (25**2 + 2**2 + 5**2)
print(s_norm)
s_norm = np.dot(x,x)
print(s_norm)
x_t = x.T
s_norm = np.sum(x * x_t)
print(s_norm)

# MAX NORM
max_norm = np.max([np.abs(25), np.abs(2), np.abs(5)])
print(max_norm)
