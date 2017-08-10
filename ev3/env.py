#!/usr/bin/env python3

#from ev3dev.ev3 import *
from time import sleep
import zmq
import random

#ir = InfraredSensor()
#ir.mode = 'IR-PROX'
context = zmq.Context()
s = context.socket(zmq.REQ)
s.connect("tcp://192.168.1.79:5376")

while True:
#	d = str (ir.value())
#	print (type(d))
	s.send_string('dssdas')
	m=s.recv()
	print (m)
	sleep(1)
