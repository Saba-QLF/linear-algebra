# WITH NUMPY
import numpy as np
x_np = np.array([25, 2, 5])
print(x_np)
print(len(x_np))
print(x_np.shape)
print(x_np[0])
print(type(x_np))
print(type(x_np[0]))

x_npt = x_np.T
print(x_npt)
# it can not transpose the tensor. Bc it is 1D array. we can do this with this method:
y_np = np.array([[25, 2, 5]])
y_npt = y_np.T
print(y_npt)
print(y_np.shape)
print(y_npt.shape)

z = np.zeros((3, 1))
o = np.ones((3, 1))
print(z)
print(o)
print(type(z[0][0]))

print("_______________________________________________")

# WITH TORCH
import torch
x_pt = torch.tensor([25, 2, 5])
print(x_pt)

print("_______________________________________________")

# WITH TENSORFLOW
import tensorflow as tf
x_tf = tf.Variable([25, 2, 5])
print(x_tf)