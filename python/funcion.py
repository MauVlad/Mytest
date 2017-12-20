a = float(input("A = ", ))
r = float(input("R = ", ))
v = float(input("V = ", ))

if a == 0:
	a = v/r
print 'A =', a

if r == 0:
	r = v/a
print 'R =', r

if v == 0:
	v = a*r
print 'V =', v
