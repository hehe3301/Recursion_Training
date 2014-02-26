import turtle


def ready(rad):
    turtle.speed(0)
    turtle.ht()
    turtle.up()
    turtle.goto(0,-rad)
    turtle.down()
    turtle.colormode(1)
    turtle.bgcolor('black')
    turtle.pensize(1.1)

def drawcircle(depth,rad,maxdepth):
    if depth == 0:
        pass
    elif depth%2==1:
        colorset(depth,maxdepth)
        turtle.circle(rad,90)
        drawcircle(depth-1,41.4*rad/100,maxdepth)
        colorset(depth,maxdepth)
        turtle.circle(rad,90)
        drawcircle(depth-1,41.4*rad/100,maxdepth)
        colorset(depth,maxdepth)
        turtle.circle(rad,90)
        drawcircle(depth-1,41.4*rad/100,maxdepth)
        colorset(depth,maxdepth)
        turtle.circle(rad,90)
        drawcircle(depth-1,41*rad/100,maxdepth)
        colorset(depth,maxdepth)
    else:
        colorset(depth,maxdepth)
        turtle.circle(rad,360/3)
        drawcircle(depth-1,46.1*rad/100,maxdepth)
        colorset(depth,maxdepth)
        turtle.circle(rad,360/3)
        drawcircle(depth-1,46.1*rad/100,maxdepth)
        colorset(depth,maxdepth)
        turtle.circle(rad,360/3)
        drawcircle(depth-1,46.1*rad/100,maxdepth)

def colorset(depth,maxdepth):
    x,y=turtle.pos()
    R=((depth-1)/maxdepth)
    G=(x*x + y*y)/(300*300)
    B=((maxdepth-depth+1)/maxdepth)
    turtle.pencolor((R,G,B))
    
def main():
    rad=250
    depth=6
#    rad=int(input('What max radius do you want to use? '))
#    depth=int(input('What depth do you want to draw? '))
    ready(rad)
    drawcircle(depth,rad,depth)
    turtle.up()
    turtle.goto(-250,-250)
    turtle.down()
    turtle.write('Alex Habermann')
main()
