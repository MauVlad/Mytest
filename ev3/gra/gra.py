import matplotlib.pyplot as plt
import math as mt
import numpy as np

j,k = 0,0
an,d = 0,0

while True:

	c = float(input('valor de hipotenusa: '))

	d = d + an
	a = c*mt.cos(mt.radians(d))
	b = c*mt.sin(mt.radians(d))

	x =(j,(a + j))
	y =(k,(b + k))
	print (x,y)

	plt.figure('plot')
	plt.plot(x,y)
#	plt.show()
	plt.savefig('lgra.jpg')
	j,k = (a + j,b + k)
	an = float(input('valor del angulo: '))
