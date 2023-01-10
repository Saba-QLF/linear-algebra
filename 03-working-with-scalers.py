# we can define a scaler (or any tensors) with python base, numpy, pytorch, tensorflow

# WITH PYTHON BASE
x = 30
y = 2.9
print(type(x))
print(type(y))

print("_______________________________________________")

# WITH PYTHORCH:
# import torch
# x_pt = torch.tensor(25)
# print(x_pt)
# print(x_pt.shape)

# print("_______________________________________________")

# WITH TENSORFLOW
import tensorflow as tf
x_tf = tf.Variable(25, dtype=tf.int16)
print(x_tf)
print(x_tf.shape)
y_tf = tf.Variable(8, dtype=tf.int16)
print(x_tf + y_tf)
tf_sum = tf.add(x_tf, y_tf)
print(tf_sum)



