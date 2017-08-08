import turtle

alex = turtle.Turtle()


while True:

	v = float (input ('magnitud: '))
	alex.forward(v)
	x=alex.xcor()
	y=alex.ycor()
	print(alex.pos())
	print (x,y)
	an = float(input ('angulo: '))
	alex.left(an)
#	alex.getcanvas().postscript(file = "fil.jpg")
#	alex.savefig('fil.jpg')
#exit()
