#!/usr/bin/env python3

##from ev3dev.ev3 import *
##from time import sleep
import zmq

##ir = InfraredSensor()
#ir.mode = 'IR-PROX'
context=zmq.Context()
socket=context.socket(zmq.REQ)
#s1=context.socket(zmq.REQ)
#s2=context.socket(zmq.REQ)
socket.connect("tcp://52.173.88.125:3003")
#s1.connect("tcp://52.173.88.125:3004")
#s2.connect("tcp://52.173.88.125:3003")

while True:
	de = float (input("1 0 2: "))

	if de == 2:

		d = float (input("escribe un numero: "))
		print (type(d))
		#s.send_string("Primer Numero: "+ str(d))
		#m=s2.recv()
		#print (m)
		s = float (input("escribe otro numero: "))
		print (type(s))
		#s1.send_string("Segundo Numero: "+ str(s))
		#m=s1.recv()
		#print (m)
		a = str(d + s)
		print (a)
		print (type(a))
		socket.send_string("la suma de : "+str(d)+' + '+str(s)+' es '+ a)
		m=socket.recv()
		print (m)

	elif de == 3:
		print("Cerrado")
		break 

	else:
		m = "nada"
		socket.send_string(m)
		print (m)
		m=socket.recv()
		print (m)
