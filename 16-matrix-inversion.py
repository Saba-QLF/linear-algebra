import numpy as np
import torch
import tensorflow as tf

# WITH NUMPY
x_np = np.array([[4, 2], [-5, -3]])
Xinv_np = np.linalg.inv(x_np)
print(Xinv_np)
y_np = np.array([4, -7])
w_np = np.dot(Xinv_np, y_np)
print(w_np)

# WITH TORCH
x_pt = torch.tensor([[4, 2], [-5, -3]], dtype=torch.float32)
print(torch.inverse(x_pt))

# WITH TENSORFLOW
x_tf = tf.Variable([[4, 2], [-5, -3]], dtype=tf.float32)
print(tf.linalg.inv(x_tf))
