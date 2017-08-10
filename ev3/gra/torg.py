import turtle
import random
from sys import exit
from time import clock
import canvasvg
turtle.colormode(255)
red = 125
green = 70
blue = 38
pen = 10
def saveImg():
    print("Done.")
    save = input("Would you like to save this tree? Y/N \n")
    if save.upper() == "Y":
        t.hideturtle()
        name = input("What would you like to name it? \n")
        nameSav = name + ".svg"
        ts = turtle.getscreen().getcanvas()
        canvasvg.saveall(nameSav, ts)
    elif save.upper() == "N":
        def runChk():
            runAgain = input("Would you like to run again? Y/N (N will exit)")
            if runAgain.upper() == "Y":
                print("Running")
                main()
            elif runAgain.upper() == "N":
                print("Exiting...")
                exit()
            else:
                print("Invalid response.")
                runChk()
        runChk()
    else:
        print("Invalid response.")
        saveImg()

def tree(branchLen, t, red, green, blue, pen):
    time = str(round(clock()))
    print("Drawing... " + time)
    if branchLen > 3:
        pen = pen*0.8
        t.pensize(pen)
        if (red > 10 and green < 140):
            red = red - 15
            green = green + 8
    if branchLen > 5:
        angle = random.randrange(18, 55)
        angleTwo = 0.5*angle
        sub = random.randrange(1,16)
        t.color(red, green, blue)
        t.forward(branchLen)
        t.right(angleTwo)
        tree(branchLen-sub,t, red, green, blue, pen)
        t.left(angle)
        tree(branchLen-sub, t, red, green, blue, pen)
        t.right(angleTwo)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    print("Please wait while I draw...")
    tree(random.randrange(60,95),t,red,green,blue, pen)
    saveImg()
main()
