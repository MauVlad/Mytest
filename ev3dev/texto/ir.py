#import ev3dev.ev3 as ev3

from ev3dev import *

ir = InfraredSensor()

print (ir.value())

print (ir.bin_data('<b'))

def grabartxt():
	archi=open('irdatos.txt','a')
	archi.write(ir.value())
	archi.write(' \n')
	archi.close()

grabartxt()
