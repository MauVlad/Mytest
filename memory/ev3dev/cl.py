#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

cl = ColorSensor()
assert cl.connected, "Connect an EV3 color sensor to any sensor port"

ts = TouchSensor()
assert ts.connected, "Connect a touch sensor to any sensor port"

#m = MediumMotor('outA')
#assert m.connected, "Connect a Medium motor to port A"

#cl.mode = 'COL-AMBIENT'
#cl.mode = 'COL-REFLECT'
cl.mode = 'COL-COLOR'

#m.run_forever(speed_sp = 0)
colors = ('desconocido','negro','azul','verde','amarillo','rojo','blanco','marron')

while not ts.value():

#	m.speed_sp = cl.value()
	print (colors[cl.value()])
	print (cl.value())
	sleep(1)

##Sound.beep()
