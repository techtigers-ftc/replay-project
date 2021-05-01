from machine import Pin
from neopixel import NeoPixel
import utime 
np = None

def init(pin = 23, length = 512):
    global np
    np = NeoPixel(Pin(pin),length)

def light_one(x):
    global np
    np.fill((0,0,0))
    np[x] = (0,0,128)
    np.write()

def light_all(length=512,time=100):
    for x in range(length):
        light_one(x)
        utime.sleep_ms(time)

def explosion(length=512, time=10):
    global np
    init()
    BLUE = (0,0,256)
    beg = 0
    end = length -1
    for x in range(length/2):
        np[beg] = BLUE
        np[beg+1] = BLUE
        np[beg+2] = BLUE
        np[beg+3] = BLUE
        np[beg+4] = BLUE
        np[beg+5] = BLUE

        np[end] = BLUE
        np[end-1] = BLUE
        np[end-2] = BLUE
        np[end-3] = BLUE
        np[end-4] = BLUE
        np[end-5] = BLUE

        beg +=1
        end -=1

        np.write()
        utime.sleep_ms(time)

    print("EXPLOSIONNNNNNNN")



  
