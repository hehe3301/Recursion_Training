from mystuff import *
from random import *



def canDraw1(level,size):
    if level==1:
        recCircle(level-1,size/2)
    else:
        R(180)
        recCircle(level-1,size/2)
        R(180)


def canDraw2(level,size):
    if level==1:
        recCircle(level-1,(randint(70,100)/100)*size/2)
    else:
        R(180)
        recCircle(level-1,(randint(70,100)/100)*size/2)
        R(180)



def recCircle(level,size):
    if level<=0:
        pass
    else:
        turtle.circle(size,90)
        canDraw1(level,size)
        turtle.circle(size,90)
        canDraw1(level,size)
        turtle.circle(size,90)
        canDraw1(level,size)
        turtle.circle(size,90)

def main(depth):
    turtle.speed(0)
    U()
    size=100
    turtle.setpos(0,-size)
    D()
    recCircle(depth,size)
    input("PAUSED")
    turtle.clear()
main(4)

