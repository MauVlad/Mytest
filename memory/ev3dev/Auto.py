#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep

ir = ev3.InfraredSensor()

m1 = ev3.LargeMotor('outB')
m2 = ev3.LargeMotor('outC')

while True:

	v = ir.value()

	if v >= 35:

		print (v, "lejos")
		m1.run_forever(speed_sp=300)
		m2.run_forever(speed_sp=300)
		sleep(1)
	else:

		print ( v, "cerca")
		m1.run_timed(time_sp=1500, speed_sp=-300, stop_action='brake')
		m2.run_timed(time_sp=3000, speed_sp=-300, stop_action='brake')
		m1.wait_while('runnig')
		m2.wait_while('runnig')
		sleep(1)
