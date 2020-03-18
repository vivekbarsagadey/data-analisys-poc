import tensorflow as tf
print(tf.__version__)
name  = tf.Variable("My name is vivek", tf.string)

rank1_tensor = tf.Variable([[1,2,2],[1,3,2]],tf.int32)

tf.print(name)
print(tf.rank(rank1_tensor))
print(rank1_tensor.shape)

tensor1 = tf.ones([1,2,3])
print(tensor1)
tensor2 = tf.reshape(tensor1,[2,3,1])
print(tensor2)
tensor3 = tf.reshape(tensor2,[3,-1])
print(tensor3)
tensor4 = tf.zeros([5,5,5,5])
print(tensor4)
tensor5 = tf.reshape(tensor4,[25,-1])
print(tensor5)
