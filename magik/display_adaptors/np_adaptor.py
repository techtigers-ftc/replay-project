from .base_display_adaptor import BaseDisplayAdaptor
from neopixel import NeoPixel
from machine import Pin

def convert_to_index(x, y, row_count):
       if (x % 2) == 0:
           return (row_count * x) + y
       else:
           return (row_count * x) + row_count - y - 1

class NeoPixelAdaptor(BaseDisplayAdaptor):
    def __init__(self):
        """ Ascii Adaptor class takes the display object and convert it into an 
        ascii display.
        """
        super().__init__()
     

    def setup(self, display_data):
        """Overides the base class
        """        
        self._grid = NeoPixel(Pin(23), 64)


    def show(self, delta, display_data):
        """ Show function will show the ascii display using the given display 
        object. Is used every loop in Controller.

        :param display: Instance that will be converted
        :type display: Display
        :param delta: The amount of time that has passed since the start of the 
        loop in the controller
        :type delta: Number
        """
        pixels = display_data.pixels

        for y_index in range(display_data.height):
            for x_index in range(display_data.width):
                led_index = convert_to_index(x_index, y_index,
                                                        display_data.height)
                self._grid[led_index] = pixels[x_index][y_index]
        self._grid.write()
