""" Initialization for the input adaptors module """

from .base_input_adaptor import BaseInputAdaptor

try:
    from .keyboard_adaptor import KeyboardAdaptor as DefaultAdaptor
except:
    from .gpio_adaptor import GPIOAdaptor as DefaultAdaptor
