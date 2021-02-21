from .base_input_adaptor import BaseInputAdaptor
from machine import Pin, ADC
#import time

OUTPUT_PIN_NUMBERS = [ 13, 12, 14, 27 ]
INPUT_PIN_NUMBERS = [ 39, 32 ]

class PressureSensorAdaptor(BaseInputAdaptor):
    def __init__(self):
        super().__init__()


    def __calibrate(self):
         for inp in inputs:
        inp.atten(ADC.ATTN_0DB)
      
        ref_1 = read_pressure(outputs, inputs)
        sleep(0.1)
        ref_2 = read_pressure(outputs, inputs)
        sleep(0.1)        
        ref_3 = read_pressure(outputs, inputs)
        sleep(0.1)
        ref_4 = read_pressure(outputs, inputs)
        sleep(0.1)        
        ref_5 = read_pressure(outputs, inputs)
        ref_avg = []
        for sensor in range(0, 4):
        ref_sum = int((ref_1[sensor] + ref_2[sensor] + ref_3[sensor] + ref_4[sensor] + ref_5[sensor])/5)
        ref_avg.append(ref_sum)
        while True:
        current = read_pressure(outputs, inputs)
        is_on = [ False, False, False, False ]
        for index in range(len(current)):
            current[index] -= ref_avg[index]
            is_on[index] = (current[index] > thresholds[index])
        
        print(ref_avg)  
        print(current) 
        print(thresholds)
        print(is_on)
        print('-----')

    def __read_pressure(self):
        result = []

        for output_pin in self._output_pins:
            output_pin.on()
            for input_pin in self._input_pins:
                result.append(input_pin.read())
            output_pin.off()

        return result

    
    def setup(self, input_data):
        """Overiden from base class
        """

        self._output_pins = []
        self._input_pins = []

        for pin_index in range(input_data.width):
            output_pin_number = OUTPUT_PIN_NUMBERS[pin_index]
            pin = Pin(output_pin_number, Pin.OUT)
            self._output_pins.append(pin)
        

        for pin_index in range(input_data.height):
            input_pin_numer  = INPUT_PIN_NUMBER[pin_index]
            pin = Pin(input_pin_number, Pin.IN)
            adc = ADC(pin)
            self._input_pins.append(adc)

    

    def read(self, delta, input_data):
        pass
        # if self.input_pin_1.read() < 4000:

        #     input_data.set_input(0, 0, 1)

        # if self.input_pin_2.read() < 4000:
        #     input_data.set_input(1, 0, 1)

        # if self.input_pin_3.read() < 4000:
        #     input_data.set_input(2, 0, 1)

        # if self.input_pin_4.read() < 4000:
        #     input_data.set_input(3, 0, 1)

        # if self.input_pin_5.read() < 4000:
        #     input_data.set_input(0, 1, 1)

        # if self.input_pin_6.read() < 4000:
        #     input_data.set_input(1, 1, 1)

        # if self.input_pin_7.read() < 4000:
        #     input_data.set_input(2, 1, 1)

        # if self.input_pin_8.read() < 4000:
        #     input_data.set_input(3, 1, 1)
               
    
