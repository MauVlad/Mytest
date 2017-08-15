#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

m_i = LargeMotor ('outB') ## Motor izquierdo
m_d = LargeMotor ('outC') ## Motor derecho
m_i.position = 0
m_d.position = 0

m_i.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
m_d.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
m_i.wait_while('runnig')
m_d.wait_while('runnig')
pos =(((m_i.position)+(m_d.position))/2)
print (pos)

m_i.run_timed(time_sp=1000, speed_sp=-525, stop_action='brake')
m_d.run_timed(time_sp=1000, speed_sp=525, stop_action='brake')
m_i.wait_while('runnig')
m_d.wait_while('runnig')
pos =(((m_i.position)+(m_d.position))/2)
print (pos)

m_i.run_timed(time_sp=750, speed_sp=350, stop_action='brake')
m_d.run_timed(time_sp=750, speed_sp=-350, stop_action='brake')
m_i.wait_while('runnig')
m_d.wait_while('runnig')
pos =(((m_i.position)+(m_d.position))/2)
print (pos)

m_i.run_timed(time_sp=500, speed_sp=-525, stop_action='brake')
m_d.run_timed(time_sp=500, speed_sp=525, stop_action='brake')
m_i.wait_while('runnig')
m_d.wait_while('runnig')
pos =(((m_i.position)+(m_d.position))/2)
print (pos)

m_i.run_timed(time_sp=2000, speed_sp=-525, stop_action='brake')
m_d.run_timed(time_sp=2000, speed_sp=525, stop_action='brake')
m_i.wait_while('runnig')
m_d.wait_while('runnig')
pos =(((m_i.position)+(m_d.position))/2)
print (pos)

m_i.run_timed(time_sp=3000, speed_sp=350, stop_action='brake')
m_d.run_timed(time_sp=3000, speed_sp=-350, stop_action='brake')
m_i.wait_while('runnig')
m_d.wait_while('runnig')
pos =(((m_i.position)+(m_d.position))/2)
print (pos)
