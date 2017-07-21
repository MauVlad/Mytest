
from time import sleep

while True:

	bat = open('/sys/class/power_supply/legoev3-battery/voltage_now', 'rb')
	bat = float(bat.read())
	bat = bat / 1000000
	print (bat)	
	print (type(bat))
	
	if bat < 5:
		print ("bateria baja")

		sleep(10)

