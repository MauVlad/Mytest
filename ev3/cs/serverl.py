#!/usr/bin/env python3

##Librerias a usar##
import matplotlib.pyplot as plt
import math as mt
import zmq
from time import sleep

##Declaramos el contexto y creamos los Socket##
context = zmq.Context()
s = context.socket(zmq.REP)
s1 = context.socket(zmq.REP)
s2 = context.socket(zmq.REP)
s3 = context.socket(zmq.REP)

##Direcion y puerto##
s.bind("tcp://192.168.1.79:7535")
s1.bind("tcp://192.168.1.79:6763")
s2.bind("tcp://192.168.1.79:6625")
s3.bind("tcp://192.168.1.79:5376")

##Parametros iniciales##
j,k = 0,0
d = 0

##Entrando al ciclo##
while True:

	m=s.recv()
	print (m)
	s.send_string('enviado')

	m1=s1.recv()
	print (m1)
	s1.send_string('enviado')

#	m2=s2.recv()
#	s2.send_string('enviado')
#	print(m2)

#	m3=s3.recv()
#	print(m3)
#	s3.send_string('enviado')

#	c = float(m)
#	an = float(m1)
#	d = d + an
#	a = c*mt.cos(mt.radians(d))
#	b = c*mt.sin(mt.radians(d))

#	x =(j,(a + j))
#	y =(k,(b + k))
#	print (x,y)

#	plt.plot(x,y)
#	plt.savefig('lgra.jpg')
#	j,k = (a + j,b + k)
#	an = float(m2)

