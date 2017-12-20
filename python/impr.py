x = int(input("1.- T(1) o F(0) = "))
x1 = int(input("2.- T(1) o F(0) = "))

print "Motrar: todo, and, or : "
y = raw_input("Palabra : ")

if x == 1:
	a=True
if x1 == 1:
	b=True
if x == 0:
	a=False
if x1 == 0:
	b=False

print x, x1, y

if y == 'todo':
	print "and : ", a and b
	print "and 'a negada' y 'b' : ", (not a) and b
	print "and 'a' y 'b negada' : ", a and (not b)
	print "or : ", a or b
	print "or 'a negada' y 'b' : ", (not a) or b
	print "or 'a' y 'b negada' :  ", a or (not b)

if y == 'and':
	print "and", a and b

if y == 'or':
	print "or", a or b
