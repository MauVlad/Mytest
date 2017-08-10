#!/usr/bin/env python3
#from ev3dev.ev3 import *

def limit_speed(speed):
	if speed > 800:
		speed = 800
	elif speed < 350:
		speed = 350
	return speed

#ir = InfraredSensor()
#assert ir.connected, "Error conecte Infraredsensor"

#ts = TouchSensor()
#assert ts.connected, "Error conecte Touchsensor"

#m1 = LargeMotor(OUTPUT_B)
#m2 = LargeMotor(OUTPUT_C)

X_REF = 120
Y_REF = 150
KP = 0.4 #0.4
KI = 0.01 #0.01
KD = 0.005 #0.005
GAIN = 10 #10

integral_x = 0
derivative_x = 0
last_dx = 0
integral_y = 0
derivative_y = 0
last_dy = 0

while True: #not ts.value():
	v = float(input("ingresa un valor: "))

	if v > 30: #ir.value() > 30:
		x = v #ir.value()
		y = v #ir.value()
		dx = X_REF - x
		integral_x = integral_x + dx
		derivative_x = dx - last_dx
		speed_x = KP*dx + KI*integral_x + KD*derivative_x
		dy = Y_REF - y
		integral_y = integral_y + dy
		derivative_y = dy - last_dy
		speed_y = KP*dy + KI*integral_y + KD*derivative_y

#		m1.run_forever(speed_sp = limit_speed(GAIN * (speed_y + speed_x)))
#		m2.run_forever(speed_sp = limit_speed(GAIN * (speed_y - speed_x)))
		speed_sp = limit_speed(GAIN * (speed_y + speed_x))
		print(speed_sp,speed_y,speed_x)
		speed_sp = limit_speed(GAIN * (speed_y + speed_x))
		print(speed_sp,speed_y,speed_x)
		last_dx = dx
		last_dy = dy
	else:
		print ("fin")
		integral_x = 0
		integral_y = 0
#		m1.stop()
#		m2.stop()


m1.stop()
m2.stop()
