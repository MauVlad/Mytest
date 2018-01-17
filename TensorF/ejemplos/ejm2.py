import tensorflow as tf

x = tf.constant(1.0, name='input')
w = tf.Variable(0.8, name='weight')
y = tf.multiply(w, x, name='output')

##summary_writer = tf.train.SummaryWriter('log_simple_graph', sess.graph)
summary_writer = tf.summary.FileWriter('log_simple_graph', sess.graph)

