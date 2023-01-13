import numpy as np
import torch
import tensorflow as tf

# WITH NUMPY
X_np = np.array([[1, 2], [3, 4]])
print(np.linalg.norm(X_np))

print('-------------------------------------------')

# WITH PYTORCH
X_pt = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print(torch.norm(X_pt))

print('-------------------------------------------')

# WITH TENSORFLOW
X_tf = tf.Variable([[1, 2], [3, 4]], dtype=tf.float32)
print(tf.norm(X_tf))
