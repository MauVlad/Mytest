#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as pl
import matplotlib.animation as animation
import math as mt
import numpy as np

##a = input ('escribe un numero: ')
##b = input ('escribe otro numero: ')

#for a in [a,3,4,2,a,a]:
#b = float(input ('escribe otro numero: '))
#x = y = 0
a = b = 0

while True:

	c = float(input('valor de hipotenusa: '))
	an = float(input('valor del angulo: '))

	a = c*mt.cos(mt.radians(an))
	b = c*mt.sin(mt.radians(an))
	print(a,b)

	a = c*np.cos(np.radians(an))
	b = c*np.sin(np.radians(an))

	print(a,b)

#	z = input('d o i: ')
#	a = float(input ('escribe un numero: '))
#	b = float(input ('escribe otro numero: '))
#	print (x,y)
#	n = 10 ##1024
#	w = float(input ('angulo X: '))
#	q = float(input ('angulo Y: '))
	x = a #np.random.normal() ##(0,1,n)
	y = b  #np.random.normal() ##(0,1,n)
#	b = b + .1

	ax = pl.gca()
	angle = mt.atan2(y, x) * (180.0 / mt.pi)
	print (x,y)
	print (mt.atan2(y, x))
	print (180.0 / mt.pi)
	print('Ángulo en grados: ' + str(angle))


	pl.scatter(x,y)
#	pl.plot(x,y)
#	pl.show()
	pl.savefig('gd.jpg')
#	pl.savefig('gd.jpg')
