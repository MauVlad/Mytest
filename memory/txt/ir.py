#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time import sleep

ir = ev3.InfraredSensor()
ts = ev3.TouchSensor()


while not ts.value(): ##True:
	print (ir.value())
	sleep(0.5)
	def writetxt():
		archi=open('irdatos.txt','a')
		archi.write(str(ir.value()))
		archi.write(' \n')
		archi.close()
	writetxt()

def cltxt():
	archi=open('irdatos.txt', 'w')
	archi.close()
cltxt()
