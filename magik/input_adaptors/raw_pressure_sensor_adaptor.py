from .base_input_adaptor import BaseInputAdaptor
from machine import Pin, ADC
import utime
#import time

AVAILABLE_OUTPUT_PIN_NUMBERS = [ 13, 12, 14, 27 ]
AVAILABLE_INPUT_PIN_NUMBERS = [ 39, 32 ]
MAX_REF_VALUES = 100

class RawPressureSensorAdaptor(BaseInputAdaptor):
    """ Adapts raw inputs from pressure sensor """

    def __init__(self):
        """ Creates new instance of RawPressureSensorAdaptor """
        super().__init__()
        self.__input_pins = []
        self.__output_pins = []
        self.__width = 0
        self.__height = 0
        self._ref_avg = [[]]
    
    def _initialize_grid(self, initial_value = 0):
        grid = []
        for index in range(self.__height):
            grid.append([initial_value] * self.__width)
        return grid

    def _iterate_grid(self, grid, action):
        for row_index in range(self.__height):
            for col_index in range(self.__width):
                action(row_index, col_index, grid[row_index][col_index])


    def __calibrate(self):
        """ Calibrates the pressure sensors with average reference values """
        for inp in self.__input_pins:
            inp.atten(ADC.ATTN_0DB)

        # Capture multiple raw readings
        ref_values = []
        for index in range(MAX_REF_VALUES):
            ref_values.append(self._read_pressure())
            utime.sleep(0.01)

        # Calculate sum of raw readings
        def add_refs(row,col,val):
            ref_sum[row][col] +=val

        ref_sum = self._initialize_grid()
        for ref_value in ref_values:
            self._iterate_grid(ref_value, add_refs)

        # Calculate average of raw readings
        def avg_refs(row,col,val):
             self._ref_avg[row][col] = val/MAX_REF_VALUES

        self._ref_avg = self._initialize_grid()
        self._iterate_grid(ref_sum, avg_refs)

    def _read_pressure(self):
        """ Reads the pressure on the pressure sensors """
        result = []

        for output_pin in self.__output_pins:
            output_pin.on()
            row = []
            for input_pin in self.__input_pins:
                row.append(input_pin.read())
            output_pin.off()
            result.append(row)

        return result


    def setup(self, input_data):
        """ Initialize input and output pins based on the size of the input, and
        calibrate the input values.

        :param input_data: Reference to input data object
        :type input_data: InputData
        """

        self.__output_pins = []
        self.__input_pins = []
        self.__width = input_data.width
        self.__height = input_data.height

        for pin_index in range(self.__height):
            output_pin_number = AVAILABLE_OUTPUT_PIN_NUMBERS[pin_index]
            pin = Pin(output_pin_number, Pin.OUT)
            self.__output_pins.append(pin)


        for pin_index in range(self.__width):
            input_pin_number  = AVAILABLE_INPUT_PIN_NUMBERS[pin_index]
            pin = Pin(input_pin_number, Pin.IN)
            adc = ADC(pin)
            self.__input_pins.append(adc)

        self.__calibrate()

    def read(self, delta, input_data):
        """ Returns the raw values of the pressure sensor

        :param delta: no one uses it
        :type delta: literaly no one uses it - Rishi
        :param input_data: Reference to Input Data object
        :type input_data:InputData
        """
        current = self._read_pressure()

        def set_input(row, col, val):
            val = round(val - self._ref_avg[row][col], 2)
            input_data.set_input(row, col, val)

        self._iterate_grid(current, set_input)













