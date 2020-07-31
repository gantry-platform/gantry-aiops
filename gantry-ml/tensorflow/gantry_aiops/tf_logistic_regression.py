import tensorflow as tf
import numpy as np
tf.set_random_seed(777)

# data (CSV): 
# 0,0.08379999999998593,0.5622259218589494,0
# 171,1.6777333333333564,0.7347358779862057,1
xy = np.loadtxt('cluster.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 1:-1]
y_data = xy[:, [-1]]
print(x_data.shape, y_data.shape)

# input output 
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# Hypothesis using sigmoid: 
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

# cost fuction
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# abnormal if hypothesis>0.5 else normal
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

#Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
    #for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, cost_val)

    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)
    print("test input ::: should be 1", sess.run(hypothesis, feed_dict={X: [[1.9980000000000002, 0.2774374445897312]]}))
    print("test input ::: should be 0", sess.run(hypothesis, feed_dict={X: [[0.5418000000000014, 0.15445027502694608]]}))
    print("test input ::: should be 1", sess.run(hypothesis, feed_dict={X: [[1.9040539729735135,0.788305155932941]]}))
    print("test input ::: should be 0 cjb", sess.run(hypothesis, feed_dict={X: [[0.1, 0.1]]}))
    print("test input ::: should be 1 cjb", sess.run(hypothesis, feed_dict={X: [[1.9, 0.8]]}))
    print("test input ::: should be 1 cjb", sess.run(hypothesis, feed_dict={X: [[0.1, 0.9]]}))
    


#print("TEST abnormal (CPU Memory)", sess.run(hypothesis, feed_dict={X: [[0.1013340088932656, 0.5580860958318363]]}))
#print(sess.run(hypothesis, feed_dict={X: [[0.1, 0.5]]}))

