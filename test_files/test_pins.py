from machine import Pin, ADC
import utime

adc_pins = [ 36, 39, 34, 35, 32, 33]
new_adc_pins = [ 33, 32, 35]
adcs = []
def init():
    global adc_pins
    global adcs
    for pin in adc_pins:
        print(pin)
        adc = ADC(Pin(pin))
        adc.atten(ADC.ATTN_11DB)
        adcs.append(adc)


def read(pin_number):
    global adcs
    while True:
        print(adcs[pin_number].read())
        utime.sleep_ms(1000)
