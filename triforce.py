from mystuff import *
import random
def triangle(size,depth):
    '''
    '''
    if depth<=0:
        pass
    else:    
        D()
        triangle(size/2,depth-1)
        R(30)
        F(size/2)
        L(30)
        triangle(size/2,depth-1)
        R(30)
        F(size/2)
        R(120)
        F(size)
        R(120)
        F(size/2)
        R(90)
        triangle(size/2,depth-1)
        L(90)
        F(size/2)
        R(90)
        U()

def main():
    ready(1,0)
    turtle.colormode(255)
    size=512
    GT(-int(size/2),-int(size/2))
    depth=int(input('To what depth do you want to draw? ' ))
    triangle(size,depth)
    input('Enter to continue')
main()
