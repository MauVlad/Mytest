import matplotlib.pyplot as plt
import turtle

turtle.setup(200,200,0,0)
alex = turtle.Turtle()
j,k = 0,0

while True:

#	for i in range(4):
#		turtle.forward(100)
#		turtle.right(90)
#		a=alex.xcor()
#		b=alex.ycor()
#		x =(j,a)
#		y =(k,b)

#		plt.plot(x,y)
#		print(x,y)
#		plt.show()

	v = float (input ('magnitud: '))
	alex.forward(v)
	a=alex.xcor()
	b=alex.ycor()
	x =(j,a)
	y =(k,b)

	plt.figure('plot')
	plt.plot(x,y)
	print(x,y)
#	plt.show()
	plt.savefig('lineas.jpg')
	j,k = (a,b)

	an = float(input ('angulo: '))
	alex.left(an)



