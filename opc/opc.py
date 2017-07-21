#!/usr/bin/env python3
from ev3dev.ev3 import*
from time import sleep

m1 = LargeMotor('outB')
m2 = LargeMotor('outC')
ir = InfraredSensor()

def opc():

	m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
	m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
	m1.wait_while('runnig')
	m2.wait_while('runnig')
	sleep(2)
	x = ir.value()
	print (x)
	sleep(2)

	m1.run_timed(time_sp=3000, speed_sp=350, stop_action='brake')
	m2.run_timed(time_sp=3000, speed_sp=-350, stop_action='brake')
	m1.wait_while('runnig')
	m2.wait_while('runnig')
	sleep(2)
	y = ir.value()
	print (y)
	sleep(2)

	m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
	m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
	m1.wait_while('runnig')
	m2.wait_while('runnig')
	sleep(2)
	z = x - y
	print (z)
	sleep(2)

	if z < 0:
		print ("derecha")
	if z > 0:
		print ("izquierda")
	return 

opc()
	
print ('Finalizado')
