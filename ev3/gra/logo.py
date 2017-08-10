# coding=utf-8
__author__ = 'gaspar'

from turtle import *
import turtle


setup(600,600) #configura el tamaño de la ventana

def dibuja_rombo(velocidad):
    turtle.speed(velocidad)
    turtle.pensize(3)
    turtle.penup()
    turtle.right(70)
    turtle.forward(80)
    turtle.right(70)
    turtle.forward(15)
    turtle.pencolor("blue")
    turtle.right(165)
    turtle.pendown()
    turtle.left(30)

    for i in range(3):
        turtle.forward(150)
        turtle.left(70)


    turtle.forward(250)
    turtle.left(125)
    turtle.forward(240)
    turtle.penup()
    turtle.backward(250)
    turtle.write("Pythonizame")
    turtle.hideturtle()

def dibuja_python(velocidad):
    pl = turtle.Turtle()
    pl.speed(velocidad)
    pl.pensize(3)
    pl.fillcolor("gray")
    pl.penup()
    pl.left(70)
    pl.forward(90)
    pl.right(70)
    pl.forward(15)
    pl.pendown()
    pl.begin_fill()
    pl.backward(65)
    pl.right(70)
    pl.forward(50)
    pl.left(90)
    pl.forward(50)
    pl.backward(100)
    pl.right(90)
    pl.forward(50)
    pl.left(90)
    pl.forward(50)
    pl.left(90)
    pl.forward(25)
    pl.right(90)
    pl.forward(75)
    pl.left(90)
    pl.forward(75)
    pl.end_fill()

    # segundo python
    pl.fillcolor("gray")
    pl.begin_fill()
    pl.backward(50)
    pl.right(90)
    pl.forward(50)
    pl.right(90)
    pl.forward(50)
    pl.right(90)
    pl.forward(100)
    pl.backward(50)
    pl.left(90)
    pl.forward(50)
    pl.right(90)
    pl.forward(75)
    pl.right(90)
    pl.forward(75)
    pl.right(90)
    pl.forward(75)
    pl.left(90)
    pl.forward(50)
    pl.end_fill()
    pl.left(90)
    pl.penup()
    pl.forward(50)
    pl.pendown()
    pl.dot(10,"white")
    pl.penup()
    pl.left(90)
    pl.forward(100)
    pl.left(90)
    pl.forward(30)
    pl.pendown()
    pl.dot(10,"white")
    pl.hideturtle()


dibuja_rombo(5)
dibuja_python(5)

turtle.exitonclick() #permite que la ventana se cierre al hacer clic dentro
