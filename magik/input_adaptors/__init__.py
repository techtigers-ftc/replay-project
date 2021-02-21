""" Initialization for the input adaptors module """
import sys
from .base_input_adaptor import BaseInputAdaptor

if sys.platform == "esp32":
    from .pressure_sensor_adaptor import PressureSensorAdaptor as DefaultAdaptor
elif sys.platform == "win32":
    from .win_keyboard_adaptor import WinKeyboardAdaptor as DefaultAdaptor
else:
    from .keyboard_adaptor import KeyboardAdaptor as DefaultAdaptor
