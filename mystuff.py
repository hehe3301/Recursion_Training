
import turtle

def F(distance):
    '''
    This function defines a function F(distance) that moves the turtle forward "distance"
    Inputs: Distance
    Distance: can be any float
    '''
    turtle.forward(distance)

def R(angle):
    '''
    This function defines a function R(angle) that turns the turtle right "angle" degrees
    Inputs: angle
    angle: can be any float
    '''
    turtle.right(angle)

def L(angle):
    '''
    This function defines a function L(angle) that turns the turtle left "angle" degrees
    Inputs: angle
    angle: can be any float
    '''
    turtle.left(angle)

def B(distance):
    '''
    This function defines a function B(distance) that moves the turtle backwards "distance"
    Inputs: Distance
    Distance: can be any float
    '''
    turtle.back(distance) 


def U():
    turtle.up()

def D():
    turtle.down()
def GT(x,y):
    turtle.goto(x,y)
   
def ready(pensize,speed):
    '''
    This function picks the turtle up, orents it north on the canvas, sets the speed fast, and sets the pen to size 2
    '''
    U()
    L(90)
    turtle.speed(speed)
    turtle.pensize(pensize)

def sig(x,y):
    '''
    This function adds my signiture to the turtle drawing in a location x,y
    pre-conditions: the turtle is somwhere on the board
    post-conditions: the turtle is at the base fo my signiture
    '''
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.left(60)
    turtle.forward(23)
    turtle.left(180)
    turtle.forward(23)
    turtle.right(60)
    turtle.right(90)
    turtle.left(45)
    turtle.forward(27)
    turtle.left(135)
    turtle.forward(20)
    turtle.up()
    turtle.right(90)
    turtle.forward(15)
    turtle.down()
    turtle.right(90)
    turtle.forward(20)
    turtle.forward(-10)
    turtle.right(90)
    turtle.back(5)
    turtle.forward(60)

