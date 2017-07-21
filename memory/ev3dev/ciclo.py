# .LargeMotor = motor grande
# .MediumMotor = motor mediano

import ev3dev.ev3 as ev3

m = ev3.LargeMotor('outB')
n = ev3.LargeMotor('outC')

t = 0

while (t < 5):
	
	#m.run_timed(time_sp=5000, speed_sp=300)
	#n.run_timed(time_sp=5000, speed_sp=300)

	m.run_timed(time_sp=2000, speed_sp=300)
	n.run_timed(time_sp=2000, speed_sp=-300)

	#m.run_timed(time_sp=5000, speed_sp=300)
	#n.run_timed(time_sp=5000, speed_sp=300)

	m.run_timed(time_sp=2000, speed_sp=-300)
	n.run_timed(time_sp=2000, speed_sp=300)
	
	t = t + 1
