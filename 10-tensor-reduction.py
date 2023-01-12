import numpy as np
import torch
import tensorflow as tf

X_np = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])

# WITH NUMPY
print(X_np.sum())
print(X_np.sum(axis=0))
print(X_np.sum(axis=1))

print('--------------------------------------')

# WITH PYTORCH
print(torch.sum(X_pt))
print(torch.sum(X_pt, 0))
print(torch.sum(X_pt, 1))

print('--------------------------------------')

# WITH TENSORFLOW
print(tf.reduce_sum(X_tf))
print(tf.reduce_sum(X_tf, 0))
print((tf.reduce_sum(X_tf, 1)))