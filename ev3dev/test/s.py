import time

i = 1

while i < 20:

	print (i)
	i += 1
	time.sleep(1)
	
	if i == 10:
		print (i, "aqui")

	elif i == 18:
		print (i, "hay")

	else:
		print (i, "que no hay")
