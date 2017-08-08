import matplotlib.pyplot as plt

#plt.figure('scatter')
import math as mt
import numpy as np

j,k,d = 0,0,0

while True:

	c = float(input('valor de hipotenusa: '))
	an = float(input('valor del angulo: '))

	d = d + an
	a = c*mt.cos(mt.radians(d))
	b = c*mt.sin(mt.radians(d))
	print(a,b)

#	a = c*np.cos(np.radians(an))
#	b = c*np.sin(np.radians(an))

	print(a,b)

#	plt.figure('plot')

	x =(j,a) #np.random.rand(2)
	y =(k,b) #np.random.rand(2)
	print (x,y)
#plt.figure('scatter')
#plt.scatter(a,b)
#plt.show()
	plt.figure('plot')
	plt.plot(x,y)
#	plt.show()
	plt.savefig('lineas.jpg')
	j,k = (a,b) 
#	a,b = (a+b,b+a)
