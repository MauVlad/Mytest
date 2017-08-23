from time import sleep

z = tuple(map(float,raw_input("Numero de dos digitos: ").split(',')))

print(z,type(z))
(x,x1,xy,y1,y) = z ##90,45,0,-45,-90

lim = 4

print z

sleep(1)

for i in z:

	z = i > lim
	if i > lim:
		i = i
	else:
		i = 0
	print (z,i)
	sleep(1)

print(z)

"""if x > lim:
	x = x
	print(x,90)
else:
	x = 0
	print(x,0)
if x1 > lim:
	x1 = x1
	print(x1,45)
else:
	x1 = 0
	print(x1,0)
if y1 > lim:
	y1 = y1
	print(y1,-45)
else:
	y1 = 0
	print(y1,0)
if y > lim:
	y = y
	print(y,-90)
else:
	y = 0
	print(y,0)

if (x + x1) > (y1 + y):
	if x > x1:
		print(90)
	else:
		print(45)
elif (x + x1) < (y1 + y):

	if y > y1:
		print(-90)
	else:
		print(-45)
else:
	print("medio giro")"""


if x > x1:
	z = x
	an = 90
else:
	z = x1
	an = 45
#if z > xy:
#	z = z
#else:
#	z = xy
if z > y1:
	z
	an
else:
	z = y1
	an = -45
if z > y:
	z
	an
#elif z < y:
else:
	z = y
	an = -90
##else:
if z > 4:
	z
	an
else:
	z = 0
	an = 180

print (z,an)
