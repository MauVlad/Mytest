#!/usr/bin/env python3

##Librerias##
from ev3dev.ev3 import *
from time import sleep

##Definiendo los componentes a usar##
md = MediumMotor ('outA') ## Motor mediano
ml = LargeMotor ('outB') ## Motor izquierdo
mr = LargeMotor ('outC') ## Motor derecho

ir = InfraredSensor(); assert ir.connected, "Por favor, conecte el InfraredSensor"
ts = TouchSensor(); assert ts.connected, "Por favor, conecte el TouchSensor"
##cl = ColorSensor(); assert cl.connected, "Por favor, conecte el ColorSensor"

#Limite de velocidad de los motores##
def lim_speed(speed):
        if speed > 800:
                speed = 800
        elif speed < 450:
                speed = 450
        return speed

###
def ori():
        md.run_to_rel_pos(position_sp=175, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
        md.wait_while('runnig')
        sleep(1)

def muestra():
        md.run_to_rel_pos(position_sp=-87.5, speed_sp=350, stop_action="hold") ##Motor que gira 90 a la derecha
        md.wait_while('runnig')
        sleep(1)

#def vuelta(a,b,c):
 #       ml.run_timed(time_sp= a, speed_sp= b, stop_action='brake')
  #      print(m_i.time_sp,m_i.speed_sp)
   #     mr.run_timed(time_sp= a, speed_sp= c, stop_action='brake')
    #    print(m_d.time_sp,m_d.speed_sp)
     #   ml.wait_while('runnig')
      #  mr.wait_while('runnig')

#Datos de las ganancias##
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

        z = 0
        #an = 0
        a,b,c = 0,0,0

        v = ((ir.value()) * 0.7) ##convercion a cm de la distacia detectada

##Primera condicion por arriba de un valor de v el robot se movera##
        if v > 35:
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

                ml.run_forever(speed_sp = lim_speed(GAIN * (speed_y + speed_x)))
                mr.run_forever(speed_sp = lim_speed(GAIN * (speed_y + speed_x)))
                last_dx = dx
                last_dy = dy
##Aqui termina el PID##

##Para determinar la distacia que recorre el robot se toma como parametro la posicion de los motorres##
                pos =(((ml.position)+(mr.position))/2) ##Posicion absoluta de los dos motores
                cm =(pos * 0.0275) ##Convercion a cm por grados
                rue = (pos/360)
                print (pos,rue,cm)
##Segunda condicion para la toma de decicion##
        else:

##Se detienen los motores grandes por estar en "run_forever"
                ml.stop()
                mr.stop()

                ori()
                x = (ir.value(),1500,350,-350)
                sleep(1)
                print(x)

                muestra()
                x1= (ir.value(),750,350,-350)
                sleep(1)
                print (x1)

                muestra()

                muestra()
                y1 = (ir.value(),750,-350,350)
                sleep(1)
                print(y1)

                muestra()
                y = (ir.value(),1500,-350,350)
                sleep(1)
                print(y)

                ori()
                z = (x,y)
                z,a,b,c = max(z)

                ml.position = 0
                mr.position = 0

                ml.run_timed(time_sp= a, speed_sp= b, stop_action='brake')
                mr.run_timed(time_sp= a, speed_sp= c, stop_action='brake')
                ml.wait_while('runnig')
                mr.wait_while('runnig')


ml.stop()
mr.stop()
md.stop()
print ("Fin")
##Sound.speak('Closed program').wait()

