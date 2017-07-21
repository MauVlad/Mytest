#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

m = MediumMotor('outA')
ts = TouchSensor()

m1 = m.position = 0

while not ts.value():

	p = input("posicion en angulo: ")
	v = input("velocidad giro: ")
##	m.run_forever(speed_sp=200)
##	print (m.position)##.count_per_rot)
	m.run_to_rel_pos(position_sp= p, speed_sp= v, stop_action="hold")
	m1 = m.position
	print (m1)
	sleep(5)
