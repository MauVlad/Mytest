#encoding: utf-8

edad = int(input("edad : "))

if edad >= 0 and edad < 18:
	print "niño"
elif edad >= 18 and edad < 27:
	print "joven"
elif edad >= 27 and edad < 60:
	print "adulto"
else:
	print "viejo"
