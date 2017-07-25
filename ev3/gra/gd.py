import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
import numpy as np

ax = pl.gca()
n = 1 ##1024
x = np.random.normal(0,1)
y = np.random.normal(0,1)

pl.scatter(x,y)
pl.savefig('gd.jpg')
