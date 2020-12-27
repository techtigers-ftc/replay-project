""" Initialization for the display adaptors module """
try:
    from .ascii_adaptor import AsciiAdaptor
except:
    from .np_adaptor import NeoPixelAdaptor
