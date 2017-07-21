#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
assert cl.connected

ts = TouchSensor()
assert ts.connected

cl.mode = 'COL-COLOR'

colors = ('unknown','black','blue','green','yellow','red','white','brown')
while not ts.value():
	print(colors[cl.value()])
	Sound.speak(colors[cl.value()]).wait()
	sleep(1)
