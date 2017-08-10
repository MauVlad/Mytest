#!/usr/bin/env python3

from time import sleep
import zmq

context = zmq.Context()
s = context.socket(zmq.REP)
s.bind("tcp://192.168.1.79:5376")

while True:

	m=s.recv()
	print (m)

	s.send_string('hpola')
	sleep(1)
