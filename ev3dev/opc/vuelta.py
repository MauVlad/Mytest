#!/usr/bin/env python3
from ev3dev.ev3 import*
from time import sleep

m1 = LargeMotor('outB')
m2 = LargeMotor('outC')
ir = InfraredSensor()
assert ir.connected, "Conecte el sensor infrarojo"

v = ir.value()

if v <= 30:
	m1.stop()
	m2.stop()

if v >= 30:
	m1.run_timed(time_sp=1500, speed_sp=-300, stop_action='brake')
	m2.run_timed(time_sp=1500, speed_sp=300, stop_action='brake')
	m1.wait_while('runnig')
	m2.wait_while('runnig')
	sleep(1)
	x = ir.value()
	print x
	sleep(1)

	m1.run_timed(time_sp=3000, speed_sp=300, stop_action='brake')
	m2.run_timed(time_sp=3000, speed_sp=-300, stop_action='brake')
	m1.wait_while('runnig')
	m2.wait_while('runnig')
	sleep(3)
	y = ir.value()
	print y
	sleep(1)
	
	m1.run_timed(time_sp=1500, speed_sp=-300, stop_action='brake')
	m2.run_timed(time_sp=1500, speed_sp=300, stop_action='brake')
	m1.wait_while('runnig')
	m2.wait_while('runnig')
	sleep(1)
	z = x - y
	print z
	sleep(1)

