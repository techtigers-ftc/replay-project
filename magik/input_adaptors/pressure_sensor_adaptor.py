from .base_input_adaptor import BaseInputAdaptor
from machine import Pin, ADC
import utime
#import time

AVAILABLE_OUTPUT_PIN_NUMBERS = [ 13, 12, 14, 27 ]
AVAILABLE_INPUT_PIN_NUMBERS = [ 39, 32 ]
MAX_REF_VALUES = 100
DEBOUNCE_TIME = 250

class PressureSensorAdaptor(BaseInputAdaptor):
    """ Adapts inputs from pressure sensor """
    def __init__(self):
        """ Creates new instance of PressureSensorAdaptor """
        super().__init__()
        self.__input_pins = []
        self.__output_pins = []
        self.__width = 0
        self.__height = 0
        self.__ref_avg = [[]]
        ##300 needs to be lesser
        self.__thresholds = [[600, 500], [200, 300]]
        self.__timers = self.__initialize_grid()
    
    def __initialize_grid(self, initial_value = 0):
        grid = []
        for index in range(self.__height):
            grid.append([initial_value] * self.__width)
        return grid

    def __iterate_grid(self, grid, action):
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
            ref_values.append(self.__read_pressure())
            utime.sleep(0.01)

        # Calculate sum of raw readings
        def add_refs(row,col,val):
            ref_sum[row][col] +=val

        ref_sum = self.__initialize_grid()
        for ref_value in ref_values:
            self.__iterate_grid(ref_value, add_refs)

        # Calculate average of raw readings
        # avg_refs = lambda row, col, val: ref_avg[row][col] = val/MAX_REF_VALUES

        def avg_refs(row,col,val):
             self.__ref_avg[row][col] = val/MAX_REF_VALUES

        self.__ref_avg = self.__initialize_grid()
        self.__iterate_grid(ref_sum, avg_refs)

    def __read_pressure(self):
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

        self.__timers = self.__initialize_grid()

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
        current = self.__read_pressure()
        is_on = self.__initialize_grid(False)

        def check_on(row, col, val):
            current[row][col] -= self.__ref_avg[row][col]
            is_on[row][col] = (current[row][col] > self.__thresholds[row][col])
            # print("({},{}): {}, {}, {}, {}".format(row, col,
            #      current[row][col],
            #      self.__ref_avg[row][col],
            #      self.__thresholds[row][col],
            #      is_on[row][col]))
            # print('-----------')

        def debounce(row, col, val):
            timer_value = self.__timers[row][col]
            sensor_on = is_on[row][col]
            input_value = 0
            if timer_value == 0:
                if sensor_on:
                    self.__timers[row][col] = utime.ticks_ms()
            elif utime.ticks_diff(utime.ticks_ms(), timer_value) > DEBOUNCE_TIME:
                if sensor_on:
                    input_value = 1
                else:
                    self.__timers[row][col] = 0
            
            input_data.set_input(row, col, input_value)

        self.__iterate_grid(current, check_on)

        if is_on[1][0]:
            is_on[0][0] = False
        if is_on[1][1]:
            is_on[0][1] = False

        self.__iterate_grid(is_on, debounce)
