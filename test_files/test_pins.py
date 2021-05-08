from machine import Pin, ADC
import utime
adc_pins = [ 36, 39, 34, 35, 32, 33]
adcs = []
def init():
    global adc_pins
    global adcs
    for pin in adc_pins:
        utime.sleep(1)
        print(pin)
        adc = ADC(Pin(pin))
        adcs.append(adc)

def read(pin_number):
    global adcs
    print(adcs[pin_number].read())
