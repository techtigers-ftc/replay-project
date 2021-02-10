from machine import Pin, ADC
from time import sleep

def read_adc():
    outputs = [ Pin(13, Pin.OUT), Pin(12, Pin.OUT) ]
    inputs = [ ADC(Pin(34)),  ADC(Pin(35)) ]

    ref = read_pressure(outputs, inputs)
    while True:
        current = read_pressure(outputs, inputs)
        for index in range(len(current)):
            current[index] -= ref[index]

        print(current)
        sleep(0.5)
        
def read_pressure(outputs, inputs):
    result = [0,0,0,0]

    index = 0

    for out in outputs:
        out.on()
        for inp in inputs:
            result[index] = inp.read()
            index +=1
        out.off()

    return result
