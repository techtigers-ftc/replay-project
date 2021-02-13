""" Initialization for the display adaptors module """

from .base_display_adaptor import BaseDisplayAdaptor

try:
    from .ascii_adaptor import AsciiAdaptor as DefaultAdaptor
except:
    from .np_adaptor import NeoPixelAdaptor as DefaultAdaptor

