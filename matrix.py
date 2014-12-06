#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys

r = int(255)
g = int(0)
b = int(0)

def flashit(time_to_flash,steps):
    for j in range(0,steps):
        steps = float(steps * 1.0)
        brightness = float(j/steps)
        print j,brightness
        print time_to_flash 
        unicorn.brightness(brightness)
        unicorn.show()
        time.sleep(time_to_flash/(j+1))
    unicorn.clear()
    unicorn.brightness(0.1)

def ukfast():
    unicorn.set_pixel(0,0,51,0,153)
    unicorn.set_pixel(7,0,51,0,153)
    unicorn.set_pixel(0,1,51,0,153)
    unicorn.set_pixel(7,1,51,0,153)
    unicorn.set_pixel(0,1,51,0,153)
    unicorn.set_pixel(1,1,51,0,153)
    unicorn.set_pixel(6,1,51,0,153)
    unicorn.set_pixel(7,1,51,0,153)
    unicorn.set_pixel(0,2,51,0,153)
    unicorn.set_pixel(1,2,51,0,153)
    unicorn.set_pixel(6,2,51,0,153)
    unicorn.set_pixel(7,2,51,0,153)
    unicorn.set_pixel(0,3,51,0,153)
    unicorn.set_pixel(1,3,51,0,153)
    unicorn.set_pixel(1,4,51,0,153)
    unicorn.set_pixel(1,5,51,0,153)
    unicorn.set_pixel(1,6,51,0,153)
    unicorn.set_pixel(2,6,51,0,153)
    unicorn.set_pixel(3,6,51,0,153)
    unicorn.set_pixel(4,6,51,0,153)
    unicorn.set_pixel(5,6,51,0,153)
    unicorn.set_pixel(6,6,51,0,153)
    unicorn.set_pixel(1,6,51,0,153)
    unicorn.set_pixel(0,4,51,0,153)
    unicorn.set_pixel(0,5,51,0,153)
    unicorn.set_pixel(6,3,51,0,153)
    unicorn.set_pixel(6,4,51,0,153)
    unicorn.set_pixel(6,5,51,0,153)
    unicorn.set_pixel(7,3,51,0,153)
    unicorn.set_pixel(7,4,51,0,153)
    unicorn.set_pixel(7,5,51,0,153)
    unicorn.set_pixel(2,7,51,0,153)
    unicorn.set_pixel(3,7,51,0,153)
    unicorn.set_pixel(4,7,51,0,153)
    unicorn.set_pixel(5,7,51,0,153)

    flashit(0.05,10)
#####K#####

    unicorn.clear()
    unicorn.set_pixel(0,0,51,0,153)
    unicorn.set_pixel(0,1,51,0,153)
    unicorn.set_pixel(0,2,51,0,153)
    unicorn.set_pixel(0,3,51,0,153)
    unicorn.set_pixel(0,4,51,0,153)
    unicorn.set_pixel(0,5,51,0,153)
    unicorn.set_pixel(0,6,51,0,153)
    unicorn.set_pixel(0,7,51,0,153)
    unicorn.set_pixel(1,0,51,0,153)
    unicorn.set_pixel(1,1,51,0,153)
    unicorn.set_pixel(1,2,51,0,153)
    unicorn.set_pixel(1,3,51,0,153)
    unicorn.set_pixel(1,4,51,0,153)
    unicorn.set_pixel(1,5,51,0,153)
    unicorn.set_pixel(1,6,51,0,153)
    unicorn.set_pixel(1,7,51,0,153)
    unicorn.set_pixel(2,3,51,0,153)
    unicorn.set_pixel(2,4,51,0,153)
    unicorn.set_pixel(3,3,51,0,153)
    unicorn.set_pixel(3,4,51,0,153)
    unicorn.set_pixel(3,5,51,0,153)
    unicorn.set_pixel(4,5,51,0,153)
    unicorn.set_pixel(4,6,51,0,153)
    unicorn.set_pixel(5,6,51,0,153)
    unicorn.set_pixel(3,2,51,0,153)
    unicorn.set_pixel(4,2,51,0,153)
    unicorn.set_pixel(4,1,51,0,153)
    unicorn.set_pixel(5,1,51,0,153)
    unicorn.set_pixel(5,0,51,0,153)
    unicorn.set_pixel(5,7,51,0,153)
    unicorn.set_pixel(6,0,51,0,153)
    unicorn.set_pixel(6,7,51,0,153)
    flashit(0.05,10) 

#F 
    r = int(255)
    g = int(0)
    b = int(0)
    unicorn.set_pixel(1,0,r,g,b)
    unicorn.set_pixel(2,0,r,g,b)
    unicorn.set_pixel(3,0,r,g,b)
    unicorn.set_pixel(4,0,r,g,b)
    unicorn.set_pixel(5,0,r,g,b)
    unicorn.set_pixel(6,0,r,g,b)
    unicorn.set_pixel(7,0,r,g,b)
    unicorn.set_pixel(1,1,r,g,b)
    unicorn.set_pixel(2,1,r,g,b)
    unicorn.set_pixel(3,1,r,g,b)
    unicorn.set_pixel(4,1,r,g,b)
    unicorn.set_pixel(5,1,r,g,b)
    unicorn.set_pixel(6,1,r,g,b)
    unicorn.set_pixel(0,1,r,g,b)
    unicorn.set_pixel(0,2,r,g,b)
    unicorn.set_pixel(0,3,r,g,b)
    unicorn.set_pixel(0,4,r,g,b)
    unicorn.set_pixel(0,5,r,g,b)
    unicorn.set_pixel(0,6,r,g,b)
    unicorn.set_pixel(0,7,r,g,b)
    unicorn.set_pixel(1,2,r,g,b)
    unicorn.set_pixel(1,3,r,g,b)
    unicorn.set_pixel(1,4,r,g,b)
    unicorn.set_pixel(1,5,r,g,b)
    unicorn.set_pixel(1,6,r,g,b)
    unicorn.set_pixel(1,7,r,g,b)
    unicorn.set_pixel(2,4,r,g,b)
    unicorn.set_pixel(3,4,r,g,b)
    unicorn.set_pixel(4,4,r,g,b)
    unicorn.set_pixel(2,5,r,g,b)
    unicorn.set_pixel(3,5,r,g,b)
    flashit(0.05,10)

#a
    unicorn.set_pixel(1,2,r,g,b)
    unicorn.set_pixel(1,0,r,g,b)
    unicorn.set_pixel(2,0,r,g,b)
    unicorn.set_pixel(3,0,r,g,b)
    unicorn.set_pixel(4,0,r,g,b)
    unicorn.set_pixel(5,0,r,g,b)
    unicorn.set_pixel(6,0,r,g,b)
    unicorn.set_pixel(0,1,r,g,b)
    unicorn.set_pixel(1,1,r,g,b)
    unicorn.set_pixel(2,1,r,g,b)
    unicorn.set_pixel(3,1,r,g,b)
    unicorn.set_pixel(4,1,r,g,b)
    unicorn.set_pixel(5,1,r,g,b)
    unicorn.set_pixel(6,1,r,g,b)
    unicorn.set_pixel(7,1,r,g,b)
    unicorn.set_pixel(0,2,r,g,b)
    unicorn.set_pixel(1,2,r,g,b)
    unicorn.set_pixel(6,2,r,g,b)
    unicorn.set_pixel(7,2,r,g,b)
    unicorn.set_pixel(0,3,r,g,b)
    unicorn.set_pixel(1,3,r,g,b)
    unicorn.set_pixel(6,3,r,g,b)
    unicorn.set_pixel(7,3,r,g,b)
    unicorn.set_pixel(0,4,r,g,b)
    unicorn.set_pixel(1,4,r,g,b)
    unicorn.set_pixel(6,4,r,g,b)
    unicorn.set_pixel(7,4,r,g,b)
    unicorn.set_pixel(0,5,r,g,b)
    unicorn.set_pixel(1,5,r,g,b)
    unicorn.set_pixel(6,5,r,g,b)
    unicorn.set_pixel(7,5,r,g,b)
    unicorn.set_pixel(1,6,r,g,b)
    unicorn.set_pixel(2,6,r,g,b)
    unicorn.set_pixel(3,6,r,g,b)
    unicorn.set_pixel(4,6,r,g,b)
    unicorn.set_pixel(6,6,r,g,b)
    unicorn.set_pixel(7,6,r,g,b)
    unicorn.set_pixel(1,7,r,g,b)
    unicorn.set_pixel(2,7,r,g,b)
    unicorn.set_pixel(3,7,r,g,b)
    unicorn.set_pixel(4,7,r,g,b)
    unicorn.set_pixel(6,7,r,g,b)
    unicorn.set_pixel(7,7,r,g,b)

    flashit(0.05,10)

###### S#####
    unicorn.set_pixel(2,0,r,g,b)
    unicorn.set_pixel(3,0,r,g,b)
    unicorn.set_pixel(4,0,r,g,b)
    unicorn.set_pixel(5,0,r,g,b)
    unicorn.set_pixel(6,0,r,g,b)
    unicorn.set_pixel(7,0,r,g,b)
    unicorn.set_pixel(1,1,r,g,b)
    unicorn.set_pixel(2,1,r,g,b)
    unicorn.set_pixel(3,1,r,g,b)
    unicorn.set_pixel(4,1,r,g,b)
    unicorn.set_pixel(5,1,r,g,b)
    unicorn.set_pixel(6,1,r,g,b)
    unicorn.set_pixel(2,2,r,g,b)
    unicorn.set_pixel(3,2,r,g,b)
    unicorn.set_pixel(3,3,r,g,b)
    unicorn.set_pixel(4,3,r,g,b)
    unicorn.set_pixel(4,4,r,g,b)
    unicorn.set_pixel(5,4,r,g,b)
    unicorn.set_pixel(5,5,r,g,b)
    unicorn.set_pixel(6,5,r,g,b)
    unicorn.set_pixel(1,6,r,g,b)
    unicorn.set_pixel(2,6,r,g,b)
    unicorn.set_pixel(3,6,r,g,b)
    unicorn.set_pixel(4,6,r,g,b)
    unicorn.set_pixel(5,6,r,g,b)
    unicorn.set_pixel(6,6,r,g,b)
    unicorn.set_pixel(0,7,r,g,b)
    unicorn.set_pixel(1,7,r,g,b)
    unicorn.set_pixel(2,7,r,g,b)
    unicorn.set_pixel(3,7,r,g,b)
    unicorn.set_pixel(4,7,r,g,b)
    unicorn.set_pixel(5,7,r,g,b)
    flashit(0.05,10)

#####t###########

    unicorn.set_pixel(0,0,r,g,b)
    unicorn.set_pixel(0,1,r,g,b)
    unicorn.set_pixel(1,1,r,g,b)
    unicorn.set_pixel(0,2,r,g,b)
    unicorn.set_pixel(1,2,r,g,b)
    unicorn.set_pixel(2,2,r,g,b)
    unicorn.set_pixel(3,2,r,g,b)
    unicorn.set_pixel(4,2,r,g,b)
    unicorn.set_pixel(0,3,r,g,b)
    unicorn.set_pixel(1,3,r,g,b)
    unicorn.set_pixel(2,3,r,g,b)
    unicorn.set_pixel(3,3,r,g,b)
    unicorn.set_pixel(0,4,r,g,b)
    unicorn.set_pixel(1,4,r,g,b)
    unicorn.set_pixel(0,5,r,g,b)
    unicorn.set_pixel(1,5,r,g,b)
    unicorn.set_pixel(1,6,r,g,b)
    unicorn.set_pixel(2,6,r,g,b)
    unicorn.set_pixel(3,6,r,g,b)
    unicorn.set_pixel(4,6,r,g,b)
    unicorn.set_pixel(2,7,r,g,b)
    unicorn.set_pixel(3,7,r,g,b)
    unicorn.set_pixel(4,7,r,g,b)
    unicorn.set_pixel(5,7,r,g,b)

    flashit(0.05,10)


