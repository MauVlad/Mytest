import matplotlib.pyplot as plt

#plt.figure('scatter')
import math as mt
import numpy as np

j,k = 0,0
an,d = 0,0

while True:

	c = float(input('valor de hipotenusa: '))

	d = d + an
	a = c*mt.cos(mt.radians(d))
	b = c*mt.sin(mt.radians(d))
#	print(a,b)

#	a = c*np.cos(np.radians(an))
#	b = c*np.sin(np.radians(an))
#	print(j,k)
#	plt.figure('plot')

	x =(j,(a + j)) #np.random.rand(2)
	y =(k,(b + k)) #np.random.rand(2)
	print (a , j)
	print (b , k)
	print (x,y)

#plt.figure('scatter')
#plt.scatter(a,b)
#plt.show()
	plt.figure('plot')
	plt.plot(x,y)
#	plt.show()
	plt.savefig('lgra.jpg')
	j,k = (a + j,b + k) 
	an = float(input('valor del angulo: '))
#	a,b = (a+b,b+a)
