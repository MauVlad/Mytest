#!/usr/bin/env python3

##Librerias##
from ev3dev.ev3 import *
from time import sleep
import zmq

md = MediumMotor ('outA') ## Motor mediano
m1 = LargeMotor ('outB') ## Motor izquierdo
m2 = LargeMotor ('outC') ## Motor derecho

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

##Coneccion al servidor##
context=zmq.Context()
s=context.socket(zmq.REQ)
s.connect("tcp://52.173.88.125:3003")
#Sound.speak('Connected to server').wait()

##Datos de las ganancias##
X_REF = 130
Y_REF = 130
KP = 0.4
KI = 0.01
KD = 0.005
GAIN = 10

##Datos iniciales##
m1.position = 0
m2.position = 0

integral_x = 0
derivative_x = 0
last_dx = 0
integral_y = 0
derivative_y = 0
last_dy = 0

while not ts.value():

        v = ((ir.value()) * 0.7) ##convercion a cm

        if v > 40:
                print (ir.value(), v)
###
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

                m1.run_forever(speed_sp = lim_speed(GAIN * (speed_y + speed_x)))
                m2.run_forever(speed_sp = lim_speed(GAIN * (speed_y - speed_x)))
                last_dx = dx
                last_dy = dy
###
                md.stop()
#               m1.run_forever(speed_sp=600) ##velocidad de los motores, giro 
#               m2.run_forever(speed_sp=600) ##siempre hasta cambiar condicion
                pos =(((m1.position)+(m2.position))/2)
                cm =(pos * 0.0275) ##cm recoridos por grados

                if v <= 65:
                        def gdatos():
                                archi=open('datos/dato.txt', 'a')
                                archi.write('Objeto cercano a '+ str(v) + 'cm' + '\n')
                                archi.close()
                        s.send_string("Obejto cercano a " + str(v) + "cm")
                        m=s.recv()
                        print (m)
                        datos()

        else:

                m1.stop()
                m2.stop()
                def gdatos():
                        archi=open('datos/dato.txt', 'a')
                        archi.write('Distancia recorida antes de girar ' + str(cm) + 'cm' + '\n')
                        archi.close()
                gdatos()


                md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold")
                sleep(2)
                x = ir.value()
                print (x)
#               Sound.speak('Detection at '+ str(x)).wait()

                md.run_to_rel_pos(position_sp=-350, speed_sp=350, stop_action="hold")
                sleep(2)
                y = ir.value()
                print (y)
#               Sound.speak('Detection at '+ str(y)).wait()

                md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold")
                sleep(2)
                z = (x - y)
                print (z)
                Sound.beep()
                sleep(2)

                if z < 0:
                        Sound.speak('Left').wait()
                        print("izquierda")
                        m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
                        m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
                        m1.wait_while('runnig')
                        m2.wait_while('runnig')
                        s.send_string("Gire a la izquierda, recoriendo una distacia de " + str(cm) + "cm")
                        m=s.recv()
                        print (m)
                        m1.position = 0
                        m2.position = 0
                        def gdatos():
                                archi=open('datos/datos.txt', 'a')
                                archi.write('Gire a la izquierda '+ str(z))
                                archi.close()
                        gdatos()
                        sleep(2)
                        Sound.beep()

                elif z > 0:
                        Sound.speak('Right').wait()
                        print ("derecha")
                        m1.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
                        m2.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
                        m1.wait_while('runnig')
                        m2.wait_while('runnig')
                        s.send_string("Gire a la derecha, recoriendo una distacia de " + str(cm) + "cm")
                        m=s.recv()
                        print (m)
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



