a = int(input("%a = ", ))
b = int(input("%b = ", ))

#############################################
print "F(X)"
def f(x): return x % a != 0 and x % b != 0 
z = int(input("Nx = ", ))
y = int(input("Ny = ", ))
print filter(f,range(z, y))
#############################################
print "CUBO(X)"
z = int(input("Nx = ", ))
y = int(input("Ny = ", ))
def cubo(x): return x*x*x
print map(cubo, range(z, y))
#############################################
print "ADD(X, Y)"
z = int(input("Nx = ", ))
sec =range(z)
def add(x, y): return x+y
print map(add, sec, sec)
#############################################
print "SUMAR(X, Y)"
z = int(input("Nx = ", ))
y = int(input("Ny = ", ))
def sumar(x, y): return x+y
print reduce(sumar, range(1, 11))
#############################################
print "SUM(SEC)"
def sum(sec):
	def sumar(x,y): return x+y
	return reduce(sumar, sec, 0)
z = int(input("Nx = ", ))
y = int(input("Ny = ", ))
print sum(range(z, y))

