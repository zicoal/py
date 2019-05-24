import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.InteractiveSession()

I_matrix = tf.eye(5)

print(sess.run(I_matrix))
print(I_matrix.shape)
print(I_matrix.shape[0])

test_set_size=1
train, test = I_matrix[: -test_set_size], I_matrix[-test_set_size:]
print(sess.run(train))
print(sess.run(test))

#testmatrix=
#list(testmatrix)
#y_train=np.array(map(int, I_matrix[: -test_set_size]))
#print(y_train.shape)


a=[]
'''
x=tf.Variable(tf.eye(10))
x.initializer.run()

print(x.eval())

a=tf.Variable(tf.random_normal([5,10]))
a.initializer.run()
print(a.eval())

product = tf.matmul(a,x)

b=tf.Variable(tf.random_uniform([5,10],0,2,dtype=tf.int32))
b.initializer.run()
print(b.eval())
b_new =tf.cast(b,dtype=tf.float32)


t_sum = tf.add(product,b_new)
t_sub = product - b_new

print("A*X+b=\n",t_sum.eval())
print("A*X-b=\n",t_sub.eval())
'''