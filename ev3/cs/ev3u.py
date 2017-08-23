#!/usr/bin/env python3

##Librerias##
from ev3dev.ev3 import *
from time import sleep
import zmq

##Definiendo los componentes a usar##
md = MediumMotor ('outA') ## Motor mediano
m_i = LargeMotor ('outB') ## Motor izquierdo
m_d = LargeMotor ('outC') ## Motor derecho

ir = InfraredSensor(); assert ir.connected, "Por favor, conecte el InfraredSensor"
ts = TouchSensor(); assert ts.connected, "Por favor, conecte el TouchSensor"
##cl = ColorSensor(); assert cl.connected, "Por favor, conecte el ColorSensor"

##Definir la funcion que crea un archivo##
def datos():
        archi=open('datos/dato.txt', 'a')
        archi.write('Fecha y Hora: '+ time.strftime("%x ")+ time.strftime("%X")+ '\n')
        archi.close()

##Limite de velocidad de los motores##
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

##Coneccion al servidor##
#context=zmq.Context()
#s=context.socket(zmq.REQ)
#s1=context.socket(zmq.REQ)
#s2=context.socket(zmq.REQ)
#s3=context.socket(zmq.REQ)
#s.connect("tcp://192.168.1.79:7535")
#s1.connect("tcp://192.168.1.79:6763")
#s2.connect("tcp://192.168.1.79:6625")
#s3.connect("tcp://192.168.1.79:5376")
#Sound.speak('Connected to server').wait()

##Datos de las ganancias##
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
                pos =(((m1.position)+(m2.position))/2) ##Posicion absoluta de los dos motores
                cm =(pos * 0.0275) ##Convercion a cm por grados

##Sub-condicion para enviar datos relevantes y guardarlos##
                if v <= 65:
                        def gdatos(): ##Deficiondo la funcion de guardado de tados
                                archi=open('datos/dato.txt', 'a')
                                archi.write('Objeto cercano a '+ str(v) + 'cm' + '\n')
                                archi.close()

#                        s.send_string("Obejto cercano a " + str(v) + "cm") ##Funcion para enviar datos
#                        m=s.recv()
#                        print (m)
                        datos()
			gdatos()
#                else:
#                        s.send_string("No hay deteccion") ##Funcion para enviar datos
#                        m=s.recv()
#                        print (m)

##Segunda condicion para la toma de decicion##
        else:

##Se detienen los motores grandes por estar en "run_forever"
                m1.stop()
                m2.stop()

##Define una funcion guardado##
                def gdatos():
                        archi=open('datos/dato.txt', 'a')
                        archi.write('Distancia recorida antes de girar ' + str(cm) + 'cm' + '\n') ##Guarda la distacia recorida
                        archi.close()
		datos()
                gdatos()

##Entra en estado de verificaicon de distacia para determonar a donde girar, por medio del motor mediano##
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
			an = 90
		else:
			z = x1
			an = 45

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
			an = -45

		muestra()
		y = irvalue()
		print(y)
		if z > y:
			z = z
			an
		elif z < y:
			z = y
			an = -90
		else:
			z = 0
			an = 180


                md.run_to_rel_pos(position_sp=-175, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
                md.wait_while('runnig')


##Condicion para vuelta##
                if x < y: ##Si es menor a 0 tomara decicion de ir a la izquierda
                        Sound.speak('Left').wait()
                        print("izquierda")
                        m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
                        m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
                        md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold")
                        m1.wait_while('runnig')
                        m2.wait_while('runnig')
#                        s1.send_string("Gire a la izquierda, recoriendo una distacia de " + str(cm) + "cm")
#                        m1=s1.recv()
                        print (m1)
                        s2.send_string('90')
                        s3.send_string(str(cm))
                        m1.position = 0
                        m2.position = 0
                        def gdatos():
                                archi=open('datos/datos.txt', 'a')
                                archi.write('Gire a la izquierda '+ str(z))
                                archi.close()
                        gdatos()
                        sleep(2)
                        Sound.beep()

                elif x > y:
                        Sound.speak('Right').wait()
                        print ("derecha")
                        m1.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
                        m2.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
                        md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold") 
                        m1.wait_while('runnig')
                        m2.wait_while('runnig')
                        s1.send_string("Gire a la derecha, recoriendo una distacia de " + str(cm) + "cm")
                        m1=s1.recv()
                        print (m1)
                        s2.send_string('-90')
                        s3.send_string(str(cm))
                        m1.position = 0
                        m2.position = 0
                        def gdatos():
                                archi=open('datos/datos.txt', 'a')
                                archi.write('Gire a la derecha '+ str(z))
                                archi.close()
                        gdatos()
                        sleep(2)
                        Sound.beep()

                else:
                        m1.run_forever(speed_sp=600) ##velocidad de los motores, giro 
                        m2.run_forever(speed_sp=-600) ##siempre hasta cambiar condicion

m1.stop()
m2.stop()
print ("Fin")
##Sound.speak('Closed program').wait()


