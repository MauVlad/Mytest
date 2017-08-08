import matplotlib.pyplot as plt
import turtle

turtle.setup(200,200,5,5)
alex = turtle.Turtle()
j,k = 0,0

while True:

	v = float (input ('magnitud: '))
	alex.forward(v)
	a=alex.xcor()
	b=alex.ycor()
	x =(j,a)
	y =(k,b)

#	plt.figure('plot')
	plt.plot(x,y)
	print(x,y)
#      	plt.show()
	plt.savefig('lineas.jpg')
	j,k = (a,b)

	an = float(input ('angulo: '))
	alex.left(an)



