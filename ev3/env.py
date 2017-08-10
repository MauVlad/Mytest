#!/usr/bin/env python3

#from ev3dev.ev3 import *
from time import sleep
import zmq
import random

#ir = InfraredSensor()
#ir.mode = 'IR-PROX'
context = zmq.Context()
s = context.socket(zmq.REQ)
s1 = context.socket(zmq.REQ)
s.connect("tcp://192.168.1.79:7535")
s1.connect("tcp://192.168.1.79:6763")

an = '0'

while True:
#	d = str (ir.value())
#	print (type(d))
	v = input('magnitud: ')

	s.send_string(v)
	m=s.recv()
	print (m)
	s1.send_string(an)
	m=s1.recv()
	print (m)

#	a = (v, an)
#	print (type (a))

#	for a in a:

#		print (a)
#		s.send_string(a)
#		m=s.recv()
#		print (m)
#		sleep(1)

	an = input('angulo: ')
