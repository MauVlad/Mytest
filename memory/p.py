import ev3dev.ev3 as ev3

a = float(input("TimeA = "))
b = float(input("TimeB = "))


t = 0

while (t < 7):
 
	c = float(input("SpeedA = "))
	d = float(input("SpeedB = "))

	m = ev3.LargeMotor('outB')
	m.run_timed(time_sp= a, speed_sp=c)

	n = ev3.LargeMotor('outC')
	n.run_timed(time_sp= b, speed_sp=d)
	
	print ('t = ', t)
	t = t + 1

a = float(input("Time = "))
b = float(input("Speed = "))

m = ev3.LargeMotor('outB')
n = ev3.LargeMotor('outC')

m.run_timed(time_sp= a, speed_sp=b)
n.run_timed(time_sp= a, speed_sp=b)
