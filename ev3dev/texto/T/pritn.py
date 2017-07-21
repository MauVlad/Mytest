from time import sleep
import filecmp

"""while True:
	bat = open('/sys/class/power_supply/legoev3-battery/voltage_now', 'rb'')
	bat = float(bat.read())
	print (bat)
	print (type(bat))

	if bat < 5:
		print ("Bateria baja")
"""

a = open('n.txt', 'rb')
b = open('m.txt', 'rb')

a = int(a.read())
b = int(b.read())

print (filecmp.cmp("n.txt","m.txt", shallow=False))

print (type(a))
