import numpy as np
import torch
import tensorflow as tf

X_np = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])

# WITH NUMPY
print(X_np*2)
print(X_np/2)
print(X_np+2)
print(X_np-2)

print('------------------------------------------')

# WITH PYTORCH
print(X_pt*3)
print(X_pt/3)
print(X_pt+3)
print(X_pt-3)
# or
print(torch.mul(X_pt, 3))
print(torch.mul(X_pt, 1/3))
print(torch.add(X_pt, 3))
print(torch.add(X_pt, -3))

print('------------------------------------------')


# WITH TENSORFLOW
print(X_tf*4)
print(X_tf/4)
print(X_tf+4)
print(X_tf-4)
# or
print(tf.multiply(X_tf, 4))
print(tf.divide(X_tf, 4))
print(tf.add(X_tf, 4))
print(tf.subtract(X_tf, 4))

print('------------------------------------------')

# Element Wise product
# WITH NUMPY
A_np = X_np + 2
print(A_np)
print(A_np + X_np)
print(A_np * X_np)

print('------------------------------------------')

# WITH PYTORCH
A_pt = X_pt + 3
print(A_pt)
print(A_pt + X_pt)
print(A_pt * X_pt)

print('------------------------------------------')

# WITH TENSORFLOW
A_tf = X_tf + 4
print(A_tf)
print(A_tf + X_tf)
print(A_tf * X_tf)