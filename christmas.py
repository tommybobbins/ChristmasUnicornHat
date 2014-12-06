#!/usr/bin/env python
    
import unicornhat as unicorn
import time, colorsys
from matrix import ukfast
    
def christmas_tree():
    unicorn.brightness(0.4)
    r = int(0)
    g = int(255)
    b = int(0)
    rt = int(102)
    gt = int(51)
    bt = int(0)
    unicorn.set_pixel(0,5,255,0,0)
    unicorn.set_pixel(1,5,r,g,b)
    unicorn.set_pixel(2,5,r,g,b)
    unicorn.set_pixel(3,5,r,g,b)
    unicorn.set_pixel(4,5,r,g,b)
    unicorn.set_pixel(5,5,r,g,b)
    unicorn.set_pixel(6,5,r,g,b)
    unicorn.set_pixel(7,5,r,g,b)
    unicorn.set_pixel(1,4,r,g,b)
    unicorn.set_pixel(3,4,r,g,b)
    unicorn.set_pixel(5,4,r,g,b)
    unicorn.set_pixel(2,3,r,g,b)
    unicorn.set_pixel(4,3,r,g,b)
    unicorn.set_pixel(3,2,r,g,b)
    unicorn.set_pixel(3,1,r,g,b)
    #### Tree base
    unicorn.set_pixel(3,7,rt,gt,bt)
    unicorn.set_pixel(3,6,rt,gt,bt)
    #### Star
    unicorn.set_pixel(3,0,255,255,0)
    
    
    unicorn.set_pixel(0,5,255,0,b)
    unicorn.set_pixel(2,5,255,0,b)
    unicorn.set_pixel(4,5,255,0,b)
    unicorn.set_pixel(6,5,255,0,b)
    unicorn.set_pixel(0,4,51,0,153)
    unicorn.set_pixel(2,4,51,0,153)
    unicorn.set_pixel(4,4,51,0,153)
    unicorn.set_pixel(6,4,51,0,153)
    unicorn.set_pixel(1,3,255,0,0)
    unicorn.set_pixel(3,3,255,0,0)
    unicorn.set_pixel(5,3,255,0,0)
    unicorn.set_pixel(2,2,51,0,153)
    unicorn.set_pixel(4,2,51,0,153)
    #### Star
    unicorn.show()
    time.sleep(1)
    unicorn.brightness(0.5)
    unicorn.set_pixel(3,0,255,255,255)
    unicorn.show()
    time.sleep(0.1)
    unicorn.set_pixel(3,0,255,255,0)
    unicorn.brightness(0.4)
    unicorn.show()
    time.sleep(2)
    unicorn.set_pixel(0,5,51,0,153)
    unicorn.set_pixel(2,5,51,0,153)
    unicorn.set_pixel(4,5,51,0,153)
    unicorn.set_pixel(6,5,51,0,153)
    unicorn.set_pixel(0,4,255,0,0)
    unicorn.set_pixel(2,4,255,0,0)
    unicorn.set_pixel(4,4,255,0,0)
    unicorn.set_pixel(6,4,255,0,0)
    unicorn.set_pixel(1,3,51,0,153)
    unicorn.set_pixel(3,3,51,0,153)
    unicorn.set_pixel(5,3,51,0,153)
    unicorn.set_pixel(2,2,255,0,0)
    unicorn.set_pixel(4,2,255,0,0)
    unicorn.show()
    time.sleep(2)
    unicorn.clear()

while True:
    christmas_tree()
    ukfast()
