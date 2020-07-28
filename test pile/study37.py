from turtle import *
import turtle

class MyTurtle(turtle.Turtle) :
    def drawSquare(self) :
        for _ in range(4) :
            self.right(90)
            self.forward(100)

myt = MyTurtle()
myt.drawSquare()

turtle.done()