#!/usr/bin/env python3

import ev3dev.ev3 as ev3

from time import sleep


ir = ev3.InfraredSensor()

while True:
	v = ir.value()

	print (v)
	print ((v * .7), " cm")
	sleep(1)
#	print (ir.bin_data('<b'))

