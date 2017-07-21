#_*_coding: utf-8_*_
import zmq
from time import sleep


context=zmq.Context()
socket=context.socket(zmq.REQ)


socket.connect("tcp://52.173.88.125:3003")

a=5
b=4
suma=int(a*b)
pene=("omar",suma)
while(1):
    for i in pene:
        print i
        sleep(2)
        socket.send(str(i))
        reci=socket.recv()
        print reci

#while True:
   # socket.send_string(suma)
   # que=socket.recv()
   # print "esto me llego "+que		
