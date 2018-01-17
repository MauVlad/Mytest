import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")
x = tf.constant([3, 3, 3], shape=[1, 3])
y = tf.constant([5, 5, 5], shape=[3, 1])

diagonal = tf.diag(a) ## diag(Y)
trans = tf.transpose(a) ## transpose(Y)
mult = tf.matmul(x, y) ## matmul(Y)
##matmax = tf.matrix_determinant(a)
##matinv = tf.matrix_inverse(x)

sess = tf.Session()

print ('diagonal= \n', sess.run(diagonal, feed_dict={a: [3, 3, 3]}))
print ('transposicion= \n', sess.run(trans, feed_dict={a: [[3, 3, 3], [5, 5, 5]]}))
print ('multiplica= \n', sess.run(mult))
##print ('matrix_deter= \n', sess.run(matmax, feed_dict={a: [3, 3, 3]}))
##print ('matrix_inv= \n', sess.run(matinv))
