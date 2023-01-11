# WITH NUMPY
import numpy as np
X = np.array([[25, 2], [5, 26], [3, 7]])
print(X)
print(X.shape)
print(X.size)
# X.size = X.rows_num * X.cols_num
print(X.dtype)
print(X[:, 0])
print(X[0, :])

print("--------------------------------------------------")

# WITH PYTORCH
# in pythorch defining ia remains as same :D
import torch
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
print(X_pt)
print(X_pt.shape)
print(X_pt[0, :])

print("--------------------------------------------------")

# WITH TENSORFLOW
import tensorflow as tf
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])
print(X_tf)
print(tf.rank(X_tf))
print(tf.shape(X_tf))
print(X_tf[0, :])