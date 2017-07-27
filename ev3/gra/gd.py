import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
import numpy as np

a = input ('escribe un numero: ')
b = input ('escribe otro numero: ')

for a in [a,3,4]:

	print (a,b)
	ax = pl.gca()
	n = 10 ##1024
	x = (a) #np.random.normal() ##(0,1,n)
	y = (b) #np.random.normal() ##(0,1,n)
	#b = b + 1
	pl.scatter(x,y)
	pl.show()
	pl.savefig('gd.jpg')
