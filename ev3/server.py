#!/usr/bin/env python3

from time import sleep
import zmq
import turtle

turtle.setup(400,400,0,0)
alex = turtle.Turtle()

context = zmq.Context()
s = context.socket(zmq.REP)
s1 = context.socket(zmq.REP)
s.bind("tcp://192.168.1.79:7535")
s1.bind("tcp://192.168.1.79:6763")

v = an = '0'

while True:

	m=s.recv()
	print (m)
	s.send_string('enviado')

	m1=s1.recv()
	print (m1)

	s1.send_string('enviado')
#	print (v,an)
	alex.left(float(m1))
	alex.forward(float(m))
	x=alex.xcor()
	y=alex.ycor()
	print(alex.pos())
	print (x,y)

	sleep(1)
