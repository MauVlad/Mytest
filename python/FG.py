#Formula general

import math

print "Datos de la ecuacion:"

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

x1 = (-b + math.sqrt((b*b) - (4*a*c))) / (2*a)
print "X1 = ", x1
x2 = (-b - math.sqrt((b*b) - (4*a*c))) / (2*a)
print "X2 = ", x2
