from .raw_pressure_sensor_adaptor import RawPressureSensorAdaptor
from machine import Pin, ADC
import utime
#import time

AVAILABLE_OUTPUT_PIN_NUMBERS = [ 13, 12, 14, 27 ]
AVAILABLE_INPUT_PIN_NUMBERS = [ 39, 32 ]
MAX_REF_VALUES = 100
DEBOUNCE_TIME = 250

class PressureSensorAdaptor(RawPressureSensorAdaptor):
    """ Adapts inputs from pressure sensor """
    def __init__(self):
        """ Creates new instance of PressureSensorAdaptor """
        super().__init__()
        # self.__thresholds = [[601, 500], [200, 300]]

    def setup(self, input_data):
        """ Initialize input and output pins based on the size of the input, and
        calibrate the input values.

        :param input_data: Reference to input data object
        :type input_data: InputData
        """

#         RawPressureSensorAdaptor.setup(self, input_data)
#         self.__timers = self._initialize_grid()


    def read(self, delta, input_data):
        """ Sets the input data to debounced input from the pressure senson

        :param input_data: Reference to input data object
        :type input_data: InputData
        """

#         current = self._read_pressure()
#         print('-->', current[0][0], current[0][1], current [1][0], current[1][1])
#         # print('--|', self.__thresholds[0][0], self.__thresholds[0][1], self.__thresholds [1][0], self.__thresholds[1][1])
#         print('--=== ===---')
#         is_on = self._initialize_grid(False)


#         def check_on(row, col, val):
#             current[row][col] -= self._ref_avg[row][col]
#             is_on[row][col] = (current[row][col] > self.__thresholds[row][col])

#         def debounce(row, col, val):
#             timer_value = self.__timers[row][col]
#             sensor_on = is_on[row][col]
#             input_value = 0
#             if timer_value == 0:
#                 if sensor_on:
#                     self.__timers[row][col] = utime.ticks_ms()
#             elif utime.ticks_diff(utime.ticks_ms(), timer_value) > DEBOUNCE_TIME:
#                 if sensor_on:
#                     input_value = 1
#                 else:
#                     self.__timers[row][col] = 0

#             input_data.set_input(row, col, input_value)

#         self._iterate_grid(current, check_on)

#         if is_on[1][0]:
#             is_on[0][0] = False
#         if is_on[1][1]:
#             is_on[0][1] = False

#         self._iterate_grid(is_on, debounce)
