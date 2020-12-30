from .base_input_adaptor import BaseInputAdaptor
import machine
from machine import Pin, ADC
import time

class GPIOAdaptor(BaseInputAdaptor):
    def __init__(self):
        super().__init__()
        self.gpio_pin_1 = "INSERT PIN"
        self.gpio_pin_2 = "INSERT PIN"
        self.gpio_pin_3 = "INSERT PIN"
        self.gpio_pin_4 = "INSERT PIN"
        self.gpio_pin_5 = "INSERT PIN"
        self.gpio_pin_6 = "INSERT PIN"
        self.gpio_pin_7 = "INSERT PIN"
        self.gpio_pin_8 = "INSERT PIN"

        self.input_pin_1 = ADC(Pin(self.gpio_pin_1,Pin.IN))        
        self.input_pin_2 = ADC(Pin(self.gpio_pin_2,Pin.IN))        
        self.input_pin_3 = ADC(Pin(self.gpio_pin_3,Pin.IN))        
        self.input_pin_4 = ADC(Pin(self.gpio_pin_4,Pin.IN))      
        self.input_pin_5 = ADC(Pin(self.gpio_pin_5,Pin.IN))        
        self.input_pin_6 = ADC(Pin(self.gpio_pin_6,Pin.IN))        
        self.input_pin_7 = ADC(Pin(self.gpio_pin_7,Pin.IN))        
        self.input_pin_8 = ADC(Pin(self.gpio_pin_8,Pin.IN))        

    def read(self, delta, input_data):
        if self.input_pin_1.read() < 4000:

            input_data.set_input(0, 0, 1)

        if self.input_pin_2.read() < 4000:
            input_data.set_input(1, 0, 1)

        if self.input_pin_3.read() < 4000:
            input_data.set_input(2, 0, 1)

        if self.input_pin_4.read() < 4000:
            input_data.set_input(3, 0, 1)

        if self.input_pin_5.read() < 4000:
            input_data.set_input(0, 1, 1)

        if self.input_pin_6.read() < 4000:
            input_data.set_input(1, 1, 1)

        if self.input_pin_7.read() < 4000:
            input_data.set_input(2, 1, 1)

        if self.input_pin_8.read() < 4000:
            input_data.set_input(3, 1, 1)
               
    
