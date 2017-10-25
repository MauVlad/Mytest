import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

pl.plot([1,2,3])
pl.ylabel("titulo Y")
pl.savefig('ayuda.jpg')
