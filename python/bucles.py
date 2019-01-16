from time import sleep

edad = int(input ("Edad = "))
n = int(input("N = "))

while edad <= n:
	print ("tienes: " + str(edad))
	edad = int(edad) - 1
	sleep(.5)
