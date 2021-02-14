""" Initialization for the input adaptors module """
import sys
from .base_input_adaptor import BaseInputAdaptor

if sys.platform == "esp32":
    from .gpio_adaptor import GPIOAdaptor as DefaultAdaptor
elif:
    from .win_keyboard_adaptor import WinKeyboardAdaptor as DefaultAdaptor
else:
    from .keyboard_adaptor import KeyboardAdaptor as DefaultAdaptor
