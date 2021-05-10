from machine import Pin, ADC
import utime

ADC_PIN_NUMBERS = [
    33, # (0, 0)
    35, # (0, 1)
    34, # (0, 2)
    32, # (1, 0)
    36, # (1, 1)
    39  # (1, 2)
]
adcs = []
def init():
    global ADC_PIN_NUMBERS
    global adcs
    for pin in ADC_PIN_NUMBERS:
        print(pin)
        adc = ADC(Pin(pin))
        adc.atten(ADC.ATTN_11DB)
        adcs.append(adc)


def read(pin_number):
    global adcs
    while True:
        print(adcs[pin_number].read())
        utime.sleep_ms(1000)
