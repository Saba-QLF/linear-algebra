import numpy as np
import torch
import tensorflow as tf

# WITH NUMPY
A_np = np.array([[3, 4], [5, 6], [7, 8]])
b_np = np.array([1, 2])
print(np.dot(A_np, b_np))
# this method works for matrix multiplication too
print('----------------------------------------')

# WITH TORCH
A_pt = torch.tensor([[3, 4], [5, 6], [7, 8]])
b_pt = torch.tensor(([1, 2]))
print(torch.matmul(A_pt, b_pt))
# these method (like np.dot), check the size of the matrix
# and then perform dot product, matrix mul ,...
# by the size of matrices
print('----------------------------------------')

# WITH TENSORFLOW
A_tf = tf.Variable([[3, 4], [5, 6], [7, 8]])
b_tf = tf.Variable([1, 2])
print(tf.linalg.matvec(A_tf, b_tf))
# but tensorflow is different

