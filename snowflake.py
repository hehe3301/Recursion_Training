from mystuff import *
from random import *

def spoke(layer,size):
    if layer <= 1:
        pass
    elif layer%2 == 1:
        F(size)
        spoke(layer-1,size/2)
        B(size)
        L(360/3)
        F(size)
        spoke(layer-1,size/2)
        B(size)
        L(360/3)
        F(size)
        spoke(layer-1,size/2)
        B(size)
        L(360/3)
    else:
        L(360/8)
        F(size)
        spoke(layer-1,size/2)
        B(size)
        L(360/4)
        F(size)
        spoke(layer-1,size/2)
        B(size)
        L(360/4)
        F(size)
        spoke(layer-1,size/2)
        B(size)
        L(360/4)
        F(size)
        spoke(layer-1,size/2)
        B(size)
        L(360/8)
        








def main():
    spoke(7,100)
    input("Paused.")
main()
