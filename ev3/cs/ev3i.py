#!/usr/bin/env python3

##Librerias##
from ev3dev.ev3 import *
from time import sleep
import zmq

##Definiendo los componentes a usar##
md = MediumMotor ('outA') ## Motor mediano
ml = LargeMotor ('outB') ## Motor izquierdo
mr = LargeMotor ('outC') ## Motor derecho

ir = InfraredSensor(); assert ir.connected, "Por favor, conecte el InfraredSensor"
ts = TouchSensor(); assert ts.connected, "Por favor, conecte el TouchSensor"
##cl = ColorSensor(); assert cl.connected, "Por favor, conecte el ColorSensor"

##Modo de uso de los sensores##
ir.mode = 'IR-PROX'
#cl.mode = 'COL-AMBIENT'

##Crendo y definiendo los puertos de coneccion con el servidor##
context = zmq.Context()
s = context.socket(zmq.REQ)
s1 = context.socket(zmq.REQ)
s2 = context.socket(zmq.REQ)
s3 = context.socket(zmq.REQ)
s.connect("tcp://192.168.1.90:7525")
s1.connect("tcp://192.168.1.90:6763")
s2.connect("tcp://192.168.1.90:6625")
s3.connect("tcp://192.168.1.90:5376")

##Limite de velocidad de los motores##
def lim_speed(speed):
        if speed > 800:
                speed = 800
        elif speed < 450:
                speed = 450
        return speed

##Definicion de funciones para movimientos##
def ori():
        md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
        md.wait_while('runnig')
        sleep(1)

def muestra():
        md.run_to_rel_pos(position_sp=-87.5, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
        md.wait_while('runnig')
        sleep(1)

def vuelta(a,b,c):
        ml.run_timed(time_sp= a, speed_sp= b, stop_action='brake')
        mr.run_timed(time_sp= a, speed_sp= c, stop_action='brake')
        ml.wait_while('runnig')
        mr.wait_while('runnig')

##Datos de las ganancias##
X_REF = 120
Y_REF = 150
KP = 0.4
KI = 0.01
KD = 0.005
GAIN = 10

##Datos iniciales##
ml.position = 0
mr.position = 0

integral_x = 0
derivative_x = 0
last_dx = 0
integral_y = 0
derivative_y = 0
last_dy = 0

##Entrando al ciclo while##
while not ts.value():

        v = ((ir.value()) * 0.7) ##convercion a cm de la distacia detectada
###variables para dar vuelta en el mismo eje###
        z,an = 0,0
        a,b,c = 0,0,0

        s.send_string(v)
        vi=s.recv()

##Primera condicion por arriba de un valor de v el robot se movera##
        if float(vi) > 35:

		lum = cl.value()

                s1.send_string(lum)

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

###condicion para evitar el inclinamiento al desplasarce###
                mr.run_forever(speed_sp = lim_speed(GAIN * (speed_y + speed_x)))
                ml.run_forever(speed_sp = lim_speed(GAIN * (speed_y + speed_x)))

                last_dx = dx
                last_dy = dy
##Aqui termina el PID##

##Para determinar la distacia que recorre el robot se toma como parametro la posicion de los motorres##
                pos =(((ml.position)+(mr.position))/2) ##Posicion absoluta de los dos motores
                print ((ml.position),(mr.position)) ##Posicion absoluta de los dos motores
                cm =(pos * 0.0275) ##Convercion a cm por grados
                rue = (pos/360) ##convercion de grados por cm
                print (pos,rue,cm)

                s2.send_string(pos)
                cm=s2.recv()
 
                sleep(1)

##Segunda condicion para la toma de decicion##
        else:

###Se detienen los motores grandes por estar en "run_forever"###
                ml.stop()
                mr.stop()
##Funcion de ori() para la orientacion inicial del muestreo##
##Funcion de muestra() para tomar muestra cada 45 grados del giro de la cabeza##
##Funcion de vuelta() para crear el giro del robot##
                ori()
                x = (ir.value(),1500,350,-350)
                sleep(1)

                muestra()
                x1= (ir.value(),750,350,-350)
                sleep(1)

                muestra()

                muestra()
                y1 = (ir.value(),750,-350,350)
                sleep(1)

                muestra()
                y = (ir.value(),1500,-350,350)
                sleep(1)

                z = (x,x1,y1,y)
                z,a,b,c = max(z)

                def angulo(a,b,c):
                        if b > c:
                                an = a * 0.06
                        else:
                                an = a * -0.06

                        s3.send_string(an)
                        ani=s3.recv()
                        ##Sound.speak('Angle of rotation of' + ani).wait()

                angulo(a,b,c)

                vuelta(a,b,c)
###Comando que formatea la posicion de los motores para volver a comensar un nuevo trayecto##
                ml.position = 0
                mr.position = 0
                ori()

##Generacion de paros completos de los motores##
ml.stop(stop_action="hold")
mr.stop(stop_action="hold")
md.stop(stop_action="hold")

ml.stop(stop_action="brake")
mr.stop(stop_action="brake")
md.stop(stop_action="brake")

ml.stop(stop_action="coast")
mr.stop(stop_action="coast")
md.stop(stop_action="coast")

ml.stop()
mr.stop()
md.stop()
print ("Fin")
##Sound.speak('Closed program').wait()

