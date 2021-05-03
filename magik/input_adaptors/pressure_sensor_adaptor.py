from .base_input_adaptor import BaseInputAdaptor
from machine import Pin, ADC
from utime import sleep
#import time

AVAILABLE_OUTPUT_PIN_NUMBERS = [ 13, 12, 14, 27 ]
AVAILABLE_INPUT_PIN_NUMBERS = [ 39, 32 ]
MAX_REF_VALUES = 10

class PressureSensorAdaptor(BaseInputAdaptor):
    """ Adapts inputs from pressure sensor """
    def __init__(self):
        """ Creates new instance of PressureSensorAdaptor """
        super().__init__()
        self.__input_pins = []
        self.__output_pins = []
        self.__ref_avg = []
        self.__total_inputs = 0
        self.__thresholds = (1400, 1100, 220, 220)

    def __calibrate(self):
        """ Calibrates the pressure sensors with average reference values """
        for inp in self.__input_pins:
            inp.atten(ADC.ATTN_0DB)

        ref_values = []
        for index in range(MAX_REF_VALUES):
            ref_values.append(self.__read_pressure())
            sleep(0.1)

        ref_sum = [ 0 ] * self.__total_inputs
        for ref_value in ref_values:
            for index in range(len(ref_value)):
                ref_sum[index] += ref_value[index]

        self.__ref_avg = []
        for value in ref_sum:
            self.__ref_avg.append(value/MAX_REF_VALUES)

    def __read_pressure(self):
        """ Reads the pressure on the pressure sensors """
        result = []

        for output_pin in self.__output_pins:
            output_pin.on()
            for input_pin in self.__input_pins:
                result.append(input_pin.read())
            output_pin.off()

        return result


    def setup(self, input_data):
        """ Initialize input and output pins based on the size of the input, and
        calibrate the input values.

        :param input_data: Reference to input data object
        :type input_data: InputData
        """

        self.__output_pins = []
        self.__input_pins = []

        for pin_index in range(input_data.width):
            output_pin_number = AVAILABLE_OUTPUT_PIN_NUMBERS[pin_index]
            pin = Pin(output_pin_number, Pin.OUT)
            self.__output_pins.append(pin)


        for pin_index in range(input_data.height):
            input_pin_number  = AVAILABLE_INPUT_PIN_NUMBERS[pin_index]
            pin = Pin(input_pin_number, Pin.IN)
            adc = ADC(pin)
            self.__input_pins.append(adc)

        self.__total_inputs = input_data.height * input_data.width
        self.__calibrate()


    def read(self, delta, input_data):
        current = self.__read_pressure()
        is_on = [ False ] * len(current)
        for index in range(len(current)):
            current[index] -= self.__ref_avg[index]
            is_on[index] = (current[index] > self.__thresholds[index])

        input_data.set_input(0, 0, is_on[0]) 
        input_data.set_input(1, 0, is_on[1]) 
        input_data.set_input(0, 1, is_on[2]) 
        input_data.set_input(1, 1, is_on[3]) 
        print(is_on)
