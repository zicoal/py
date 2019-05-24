
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# prepare data
mnist = input_data.read_data_sets('./', one_hot=True)

print("data loaded!")

xs = tf.placeholder(tf.float32, [None, 784])
ys = tf.placeholder(tf.float32, [None, 10])

# the model of the fully-connected network
weights = tf.Variable(tf.random_normal([784, 10]))
biases = tf.Variable(tf.zeros([1, 10]) + 0.1)
outputs = tf.matmul(xs, weights) + biases
predictions = tf.nn.softmax(outputs)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(predictions),
                                              reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# compute the accuracy
correct_predictions = tf.equal(tf.argmax(predictions, 1), tf.argmax(ys, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={
            xs: batch_xs,
            ys: batch_ys
        })
        if i % 50 == 0:
            print(sess.run(accuracy, feed_dict={
                xs: mnist.test.images,
                ys: mnist.test.labels
            }))
