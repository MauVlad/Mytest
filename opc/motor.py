#!/usr/bin/env python3
from ev3dev.ev3 import*
from time import sleep
import opc

m1 = LargeMotor('outB')"derecha"
m2 = LargeMotor('outC')"izquierda"
ir = InfraredSensor()
assert ir.connected, "Conecte el sensor infrarojo"
ts = TouchSensor()
assert ts.connected;"Conecte el touchsensor"

m1.position = 0
m2.position = 0

while not ts.value():
	v = ir.value()

	if v >= 30:
		m1.run_forever(speed_sp=300)
		m2.run_forever(speed_sp=300)
		y = ((m1.position * m2.position)/2)
		cm = (y * 0.0275)
		print (v)
		print (cm,"cm")

	if v <= 30:

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
			m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
			m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
			m1.wait_while('runnig')
			m2.wait_while('runnig')

		if z > 0:
			print ("izquierda")
			m1.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
			m2.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
			m1.wait_while('runnig')
			m2.wait_while('runnig')
