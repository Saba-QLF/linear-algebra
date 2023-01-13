import numpy as np
import torch
import tensorflow as tf

# WITH NUMPY
A_np = np.array([[3, 4], [5, 6], [7, 8]])
B_np = np.array([[1, 9], [2, 0]])
print(np.dot(A_np, B_np))
print('----------------------------------------')

# WITH TORCH
A_pt = torch.tensor([[3, 4], [5, 6], [7, 8]], dtype=torch.int32)
B_pt = torch.from_numpy(B_np)
print(torch.matmul(A_pt, B_pt))

print('----------------------------------------')
# what I found:
# numpy: int32
# torch: int64

# WITH TENSORFLOW
A_tf = tf.Variable([[3, 4], [5, 6], [7, 8]])
B_tf = tf.convert_to_tensor(B_np, dtype=tf.int32)
print(tf.linalg.matmul(A_tf, B_tf))
# but tensorflow is different

