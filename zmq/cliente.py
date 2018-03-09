#!/usr/bin/env python3

#from ev3dev.ev3 import *
from time import sleep
import zmq

context = zmq.Context()
s = context.socket(zmq.REQ)
s1 = context.socket(zmq.REQ)
s2 = context.socket(zmq.REQ)
s3 = context.socket(zmq.REQ)
s.connect("tcp://192.168.1.90:7525")
s1.connect("tcp://192.168.1.90:6763")
s2.connect("tcp://192.168.1.90:6625")
s3.connect("tcp://192.168.1.90:5376")

an = '0'
def envio():
	s3.send_string(an)
	m3=s3.recv()
	print (m3)


while True:

	v = float (input('valor: '))
	print (v,type(v))

	s.send_string(str(v))
	m=s.recv()
	print (m)


	if v > 30:

		s1.send_string("luz")
		m1=s1.recv()
		print (m1)

		ma = input('magnitud: ')
		s2.send_string(ma)
		m2=s2.recv()
		print (m2)
	else:

#		an = input('angulo: ')
		s3.send_string(an)
		m3=s3.recv()
		print (m3)

		a = (ma, an)
		print (type (a))

#       for a in a:
#
#               print (a)
#               s.send_string(a)
#               m=s.recv()
#               print (m)
#               sleep(1)

		an = input('angulo: ')

