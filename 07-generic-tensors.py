import numpy as np
import torch
import tensorflow as tf

# images = [numbers, rows, columns, channels]
image_np = np.zeros([32, 28, 28, 3])
image_pt = torch.zeros([32, 28, 28, 3])
image_tf = tf.zeros([32, 28, 28, 3])
# :)
print(image_np)
print("----------------------------------------")
print(image_pt)
print("----------------------------------------")
print(image_tf)
print("----------------------------------------")
