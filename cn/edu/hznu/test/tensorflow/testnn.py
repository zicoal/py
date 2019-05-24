import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


a=[1.,3.,5.]
b=[[1.,3.,5.],[2.,4.,6.]]




def get_bias(shape):
    """
    得到每一层的bias
    :param shape:
    :return:
    """
    return tf.Variable(tf.zeros(shape))


L1 = tf.nn.tanh(a)
L2 = tf.nn.tanh(b)
bias1 = tf.placeholder(dtype=tf.float32)
bias1 = get_bias([1, 32])
init= tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run((L1)))
    print(sess.run((L2)))
    print(bias1.eval())



x = [[1, 2, 3,4],
     [2, 4, 6,8]]

xx = tf.cast(x, tf.float32)

mean_all = tf.reduce_mean(xx, keep_dims=False)
mean_0 = tf.reduce_mean(xx, axis=0, keep_dims=False)
mean_1 = tf.reduce_mean(xx, axis=1, keep_dims=False)

with tf.Session() as sess:
    m_a, m_0, m_1 = sess.run([mean_all, mean_0, mean_1])
    m =sess.run(tf.div(xx[1],xx[0]))
print(m_a)
print(m_0)
print(m_1)
print(m)
