#!/usr/bin/env python3

##Librerias a usar##
import matplotlib.pyplot as plt
import math as mt
import zmq
from time import sleep
from PIL import Image
##Declaramos el contexto y creamos los Socket##
context = zmq.Context()
s = context.socket(zmq.REP)
s1 = context.socket(zmq.REP)
s2 = context.socket(zmq.REP)
s3 = context.socket(zmq.REP)

##Direcion y puerto##
s.bind("tcp://192.168.1.90:7525")
s1.bind("tcp://192.168.1.90:6763")
s2.bind("tcp://192.168.1.90:6625")
s3.bind("tcp://192.168.1.90:5376")

##Parametros iniciales##
j,k = 0,0
d = 0

##Entrando al ciclo##
while True:

	m=s.recv()
	print (m)
	s.send_string('enviado valor')

	m = float(m)

	if m > 30:

		m1=str(s1.recv())
		print ("distacia " + str(m),m1)
		s1.send_string('enviado luz')

		m2=s2.recv()
		s2.send_string('enviado magnitud')
		print(m2)

	else:

		m3=s3.recv()
		print(m3)
		s3.send_string('enviado angulo')

		c = float(m2)
		an = float(m3)
#an = float(m3)
		d = d + an
		a = c*mt.cos(mt.radians(d))
		b = c*mt.sin(mt.radians(d))

		x =(j,(a + j))
		y =(k,(b + k))
		print (x,y)

		plt.plot(x,y)
		plt.savefig('lgra.jpg')
		j,k = (a + j,b + k)

		im = Image.open("lgra.jpg")
		im = im.resize((400,400))

		while True:

			final = Image.new("RGB",(400,400),"black")
			final.paste(im, (0,0))
			final.show()
