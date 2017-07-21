#!/usr/bin/env python3

import ev3dev.ev3 as ev3

from time import sleep

ir = ev3.InfraredSensor()

while True:

	print (ir.value())
#	sleep(0.5)

#	print (ir.bin_data('<b'))

