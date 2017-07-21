#!/usr/bin/env python3

##Librerias##
from ev3dev.ev3 import *
from time import sleep

md = MediumMotor ('outA') ## Motor mediano
m1 = LargeMotor ('outB') ## Motor izquierdo
m2 = LargeMotor ('outC') ## Motor derecho

ir = InfraredSensor(); assert ir.connected, "Por favor, conecte el Infrared"
ts = TouchSensor(); assert ts.connected, "Por favor, conecte el touchsensor"
#cl = ColorSensor(), assert cl.connected, "Por favor, conecte el sensor de color"

##Definir la funcion que crea un archivo##
def datos():
	archi=open('datos/dato.txt','a')
	archi.write('Fecha y hora: '+ time.strftime("%x")+ time.strftime("%X")+ "\n")
	archi.close()

##Parametro de posicion en 0 al inicio del programa
m1.position = 0
m2.position = 0


while not ts.value():
	
	v = ((ir.value())* .7) ## convercion de valor proximida a 'cm' 

	if v > 30 :
		m1.run_forever(speed_sp=400) ##velocidad de los motores giro por
		m2.run_forever(speed_sp=400) ##simepre hasta cambiar condicion
		pos=((m1.position + m2.position)/2)
		cm=(pos * 0.0275) ##convercion de 'valor pos' a 'cm'
		
		if v <= 65:
			def gdatos():
				archi=open('datos/dato.txt', 'a')
				archi.write('Objeto cercano a '+ v + 'cm')
				archi.close()
			datos()
			gdatos()
##	if v < 30:
	else:
		
		def gdatos():
			archi=open('datos/dato.txt', 'a')
			archi.write('Distacia recorida antes de girar' + cm + 'cm')
			archi.close()
		gdatos()

		##griro aproximado de 90° izquierda
		m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
		m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
		m1.wait_while('runnig')
		m2.wait_while('runnig')
		sleep(2)
		x = ir.value()
		print (x)
		Sound.beep()
		sleep(2)

		##griro aproximado de 180° derecha
		m1.run_timed(time_sp=3000, speed_sp=350, stop_action='brake')
		m2.run_timed(time_sp=3000, speed_sp=-350, stop_action='brake')
		m1.wait_while('runnig')
		m2.wait_while('runnig')
		sleep(2)
		y = ir.value()
		print (y)
		Sound.beep()
		sleep(2)

		##griro aproximado de 90° regreso posicion inicial
		m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
		m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
		m1.wait_while('runnig')
		m2.wait_while('runnig')
		sleep(2)
		z = x - y
		print (z)
		Sound.beep()
		sleep(2)

		if z < 0:
		##si el resultado es menor se gira a la izquierda
			Sound.speak("Izquierda").wait()
			m1.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
			m2.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
			m1.wait_while('runnig')
			m2.wait_while('runnig')
			m1.position = 0
			m2.position = 0
			def gdatos():
				archi=open('datos/dato.txt', 'a')
				archi.write('Gire a la izquierda ' + z)
				archi.close()
			gdatos()
			Sound.beep()


		if z > 0:
		##si el resutado es mayor se gira a la derecha
			Sound.speak("Derecha").wait()
			m1.run_timed(time_sp=1500, speed_sp=350, stop_action='brake')
			m2.run_timed(time_sp=1500, speed_sp=-350, stop_action='brake')
			m1.wait_while('runnig')
			m2.wait_while('runnig')
			m1.position = 0
			m2.position = 0
			def gdatos():
				archi=open('datos/dato.txt', 'a')
				archi.write('Gire a la derecha ' + z)
				archi.close()
			gdatos()
			Sound.beep()

m1.stop()
m2.stop()
Sound.speak("Programa finalizado")
