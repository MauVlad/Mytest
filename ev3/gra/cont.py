import math

x1 = 0.0
y1 = 0.0
x2 = 2.0
y2 = 2.0

x = x2 * math.cos(90) #- x1
y = y2 * math.cos(90) #- y1

angle = math.atan2(y, x) * (180.0 / math.pi)
print (math.atan2(y, x))
print (180.0 / math.pi)
print('Ángulo en grados: ' + str(angle))

#a = math.atan2(y,x)= angle/(180.0/math.pi)

"""import pylab as pl
import numpy as np

def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 26
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

pl.axes([0.025, 0.025, 0.95, 0.95])

pl.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=pl.cm.hot)
C = pl.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
pl.clabel(C, inline=1, fontsize=10)

pl.xticks(())
pl.yticks(())
pl.show()"""
