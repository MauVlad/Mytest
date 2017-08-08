import matplotlib.pyplot as pl
import math as mt
import numpy as np
import turtle

turtle.setup(200,200,0,0)

alex = turtle.Turtle()

while True:

	v = float (input ('magnitud: '))
	alex.forward(v)
	x=alex.xcor()
	y=alex.ycor()

	ax = pl.gca()
	pl.scatter(x,y)
	pl.savefig('gf.jpg')

	an = float(input ('angulo: '))
	alex.left(an)

