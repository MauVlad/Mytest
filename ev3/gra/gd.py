import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
import numpy as np

ax = pl.gca()
n = 10 ##1024
x = (1,n) ##np.random.normal() ##(0,1,n)
y = (1,n) ##np.random.normal() ##(0,1,n)

pl.scatter(x,y)
pl.savefig('gd.jpg')
