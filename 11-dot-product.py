import numpy as np
import torch
import tensorflow as tf

# WITH NUMPY
x_np = np.array([25, 2, 5])
y_np = np.array([0, 1, 2])
print(np.dot(x_np, y_np))

print('-----------------------------------')

# WITH PYTORCH
x_pt = torch.tensor([25, 2, 5], dtype=torch.float32)
y_pt = torch.tensor([0, 1, 2], dtype=torch.float32)
print(np.dot(x_pt, y_pt))
# Or
print(torch.dot(x_pt, y_pt))
# bc torch.dot only gets float points. not integers

# WITH TENSORFLOW
x_tf = tf.Variable([25, 2, 5])
y_tf = tf.Variable([0, 1, 2])
print(tf.reduce_sum(tf.multiply(x_tf, y_tf)))
