import numpy as np
import torch
import tensorflow as tf

X_np = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
X_tf = tf.Variable([[25, 2], [5, 26], [3, 7]])

# WITH NUMPY
print(X_np.T)

# WITH PYTORCH
print(X_pt.T)

# WITH TENSORFLOW
print(tf.transpose(X_tf))