from machine import Pin, ADC
from time import sleep

thresholds = (900, 900, 220, 220)

def read():
    outputs = [ Pin(13, Pin.OUT), Pin(12, Pin.OUT)  ]
    inputs = [ ADC(Pin(39)),  ADC(Pin(32)) ]

    for inp in inputs:
        inp.atten(ADC.ATTN_0DB)

    ref = read_pressure(outputs, inputs)
    while True:
        current = read_pressure(outputs, inputs)
        on = [ False, False, False, False ]
        for index in range(len(current)):
            current[index] -= ref[index]
            on[index] = (current[index] > thresholds[index])

        print(current)
        print(thresholds)
        print(on)
        print('-----')
        
def read_pressure(outputs, inputs):
    result = [0,0,0,0]

    index = 0

    for out in outputs:
        out.on()
        sleep(0.2)
        for inp in inputs:
            result[index] = inp.read()
            sleep(0.1)
            index +=1
        out.off()

    return result
