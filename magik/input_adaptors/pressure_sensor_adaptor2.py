from .base_input_adaptor import BaseInputAdaptor
from machine import Pin, ADC
import utime
#import time

ADC_PIN_NUMBERS = [
    33, # (0, 0)
    35, # (0, 1)
    34, # (0, 2)
    32, # (1, 0)
    36, # (1, 1)
    39  # (1, 2)
]
MAX_REF_VALUES = 100

class PressureSensorAdaptor2(BaseInputAdaptor):
    """ Adapts raw inputs from pressure sensor """

    def __init__(self):
        """ Creates new instance of RawPressureSensorAdaptor """
        super().__init__()
        self.__input_pins = []
        self.__width = 0
        self.__height = 0
        self._ref_avg = [[]]
    
    def _initialize_grid(self, initial_value = 0):
        grid = []
        for index in range(self.__width):
            grid.append([initial_value] * self.__height)
        return grid

    def _iterate_grid(self, grid, action):
        for x_coord in range(self.__width):
            for y_coord in range(self.__height):
                action(x_coord, y_coord, grid[x_coord][y_coord])


    def __calibrate(self):
        """ Calibrates the pressure sensors with average reference values """
        for inp in self.__input_pins:
            inp.atten(ADC.ATTN_11DB)

        # Capture multiple raw readings
        ref_values = []
        for index in range(MAX_REF_VALUES):
            ref_values.append(self._read_pressure())
            utime.sleep(0.01)

        # Calculate sum of raw readings
        def add_refs(x_coord, y_coord, val):
            ref_sum[x_coord][y_coord] +=val

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

        pin_index = 0
        for x_coord in range(self.__width):
            column = []
            for y_coord in range(self.__height):
                input_pin = self.__input_pins[pin_index]
                column.append(input_pin.read())
                pin_index += 1
            result.append(column)

        return result

    def setup(self, input_data):
        """ Initialize input and output pins based on the size of the input, and
        calibrate the input values.

        :param input_data: Reference to input data object
        :type input_data: InputData
        """

        self.__input_pins = []
        self.__width = input_data.width
        self.__height = input_data.height

        for pin_number in ADC_PIN_NUMBERS:
            pin = Pin(pin_number, Pin.IN)
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

        def set_input(x_coord, y_coord, val):
            print('Setting', x_coord, y_coord, val, 
                    self._ref_avg[x_coord][y_coord])
            val = round(val - self._ref_avg[x_coord][y_coord], 2)
            # val = round(val - 2900, 2)
            # print(val)
            input_data.set_input(x_coord, y_coord, val)

        self._iterate_grid(current, set_input)
