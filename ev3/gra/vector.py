import math as mt
import numpy as np

c = float (input('valor de hipotenusa: '))
an = float(input('valor del angulo: '))

a = c*mt.cos(mt.radians(an))
b = c*mt.sin(mt.radians(an))
print(a,b)

a = c*np.cos(np.radians(an))
b = c*np.sin(np.radians(an))

print(a,b)
