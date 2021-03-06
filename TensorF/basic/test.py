import tensorflow as tf

a = tf.placeholder("float")
b = tf.placeholder("float")

suma = tf.add(a, b) ## add(Y)
resta = tf.subtract(a, b) ## sub(N), subtract(Y)
multiplica  = tf.multiply(a, b) ## mul(N), multiply(Y)
divide = tf.div(a, b) ##div(Y), divide(Y)
flormod = tf.floor(a/b)*b+tf.mod(a, b) ##mod(Y), floormod(Y)
absoluto = tf.abs(a) ##ads(Y), numero complejos (a + bj)
negati = tf.negative(a) ##neg(N), negative(Y)
signo = tf.sign(a) ##sing(Y)
##inverso = tf.reciprocal(a) ##inv(N), inverse(N), invert()
cuadrado = tf.square(a) ##square(Y)
redondea = tf.round(a) ##round(Y)
raiz = tf.sqrt(a) ##sqrt(Y)
potencia = tf.pow(a, b) ##pow(Y)
exponencial = tf.exp(a) ##exp(Y)
logaritmo = tf.log(a) ##log()
rmax = tf.maximum(a, b)
rmin = tf.minimum(a, b)
ccos = tf.cos(a)
csin = tf.sin(a)

sess = tf.Session()

print ('suam=', sess.run(suma, feed_dict={a: 3, b: 3}))
print ('resta=', sess.run(resta, feed_dict={a: 3, b: 3}))
print ('multiplica=', sess.run(multiplica, feed_dict={a: 3, b: 3}))
print ('divide=', sess.run(divide, feed_dict={a: 3, b: 3}))
print ('absoluto=', sess.run(absoluto, feed_dict={a: 3.3}))
print ('negativo=', sess.run(negati, feed_dict={a: 3.3}))
print ('signo=', sess.run(signo, feed_dict={a: -34.3}))
##print ('inverso=', sess.run(inverso, feed_dict={a: -34.3}))
print ('cuadrado=', sess.run(cuadrado, feed_dict={a: -2}))
print ('redondea=', sess.run(redondea, feed_dict={a: 34.54}))
print ('raíz=', sess.run(raiz, feed_dict={a: 4}))
print ('potencia=', sess.run(potencia, feed_dict={a: 3, b: 2}))
print ('exponencial=', sess.run(exponencial, feed_dict={a: 2}))
print ('logaritmo=', sess.run(logaritmo, feed_dict={a: 7.38906}))
print ('maximo=', sess.run(rmax, feed_dict={a: 7, b: 8}))
print ('minimo=', sess.run(rmin, feed_dict={a: 7, b: 8}))
print ('cos=', sess.run(ccos, feed_dict={a: 90}))
print ('sin=', sess.run(csin, feed_dict={a: 90}))
