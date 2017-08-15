#!/usr/bin/env python3

##Librerias##
from ev3dev.ev3 import *
from time import sleep

##Definiendo los componentes a usar##
md = MediumMotor ('outA') ## Motor mediano
m_i = LargeMotor ('outB') ## Motor izquierdo
m_d = LargeMotor ('outC') ## Motor derecho

ir = InfraredSensor(); assert ir.connected, "Por favor, conecte el InfraredSensor"
ts = TouchSensor(); assert ts.connected, "Por favor, conecte el TouchSensor"
##cl = ColorSensor(); assert cl.connected, "Por favor, conecte el ColorSensor"

#Limite de velocidad de los motores##
def lim_speed(speed):
        if speed > 900:
                speed = 900
        elif speed < -900:
                speed = -900
        return speed

###
def muestra():
	md.run_to_rel_pos(position_sp=-87.5, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
	md.wait_while('runnig')
	sleep(1)

#Datos de las ganancias##
X_REF = 130
Y_REF = 130
KP = 0.4
KI = 0.01
KD = 0.005
GAIN = 10

##Datos iniciales##
m_i.position = 0
m_d.position = 0

integral_x = 0
derivative_x = 0
last_dx = 0
integral_y = 0
derivative_y = 0
last_dy = 0

##Entrando al ciclo while##
while not ts.value():

        v = ((ir.value()) * 0.7) ##convercion a cm de la distacia detectada

##Primera condicion por arriba de un valor de v el robot se movera##
        if v > 40:
                print (ir.value(), v)
                md.stop()

##Funcion del PID para que el motor llegue a su velocidad optima##
                x = ir.value()
                y = ir.value()
                dx = X_REF - x
                integral_x = integral_x + dx
                derivative_x = dx - last_dx
                speed_x = KP*dx + KI*integral_x + KD*derivative_x
                dy = Y_REF - y
                integral_y = integral_y + dy
                derivative_y = dy - last_dy
                speed_y = KP*dy + KI*integral_y + KD*derivative_y

                m_i.run_forever(speed_sp = lim_speed(GAIN * (speed_y + speed_x)))
                m_d.run_forever(speed_sp = lim_speed(GAIN * (speed_y + speed_x)))
                last_dx = dx
                last_dy = dy
##Aqui termina el PID##

##Para determinar la distacia que recorre el robot se toma como parametro la posicion de los motorres##
                pos =(((m_i.position)+(m_d.position))/2) ##Posicion absoluta de los dos motores
                cm =(pos * 0.0275) ##Convercion a cm por grados
		rue = (pos/360)
		print (pos,rue,cm)
##Segunda condicion para la toma de decicion##
        else:

##Se detienen los motores grandes por estar en "run_forever"
                m_i.stop()
                m_d.stop()

                md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
                md.wait_while('runnig')
                sleep(1)
		x = ir.value()
		sleep(1)
		print(x)

		muestra()
		x1= ir.value()
		sleep(1)
		print (x1)
		if x > x1:
			z = x
			an = (1500,350,-350)
		else:
			z = x1
			an = (750,350,-350)

		muestra()
		xy = ir.value()
		print(1)
		print(xy)

		muestra()
		y1 = irvalue()
		pritn(y1)
		if z > y1:
			z = z
			an
		else:
			z = y1
			an = (500,-525,525)

		muestra()
		y = irvalue()
		print(y)
		if z > y:
			z = z
			an
#		elif z < y:
		else:
			z = y
			an = (1000,-525,525)
#		else:
		if z > 35:
			an
		else:
			z = 0
			an = (2000,-525,525)

##Condicion para vuelta##
#	        Sound.speak('Left').wait()
		a,b,c = an
                m_i.run_timed(time_sp= a, speed_sp= b, stop_action='brake')
                m_d.run_timed(time_sp= a, speed_sp= c, stop_action='brake')
                md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold")
                m_i.wait_while('runnig')
                m_d.wait_while('runnig')
                m_i.position = 0
                m_d.position = 0

m_i.stop()
m-d.stop()
print ("Fin")
##Sound.speak('Closed program').wait()
