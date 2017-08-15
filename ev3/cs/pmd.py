from ev3dev.ev3 import *
from time import sleep

md = MediumMotor ('outA') ## Motor mediano

ir = InfraredSensor()
ts = TouchSensor()

def muestra():
        md.run_to_rel_pos(position_sp=87.5, speed_sp=350, stop_action$
        md.wait_while('runnig')
        sleep(1)

lim = 40

while not ts.value():
#	v = ((ir.value()) * 0.7)

	md.run_to_rel_pos(position_sp=-175, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
	md.wait_while('runnig')
	sleep(1)
	x = ir.value()
	print(x)
	muestra()
	x1= ir.value()
	print (x1)
	muestra()
	xy = ir.value()
	print(xy)
	muestra()
	y1 = irvalue()
	pritn(y1)
	muestra()
	y = irvalue()
	print(y)

	z = (x,x1,xy,y1,y)


	if x > lim:
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
		print(x,0)
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
		print("medio giro")


