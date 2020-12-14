from machine import Pin
from neopixel import NeoPixel

def get_color(rgb):
    """ This function will take a rgb tuple, and convert it into a color

    :param rgb: The rgb value that the function uses
    :type rgb: Tuple
    """
    (r, g, b) = rgb
    if r == 1:
        return (64, 0, 0)
    elif g == 1:
        return (0, 64, 0)
    elif b == 1:
        return (0, 0, 64)
    else:
        return (0, 0, 0)

def x_y_to_series_conversion(row_length, x, y):
       if (y % 2) == 0:
           return row_length*y + x
       else:
           return row_length*y + row_length - x -1

class NeoPixelAdaptor:
    def __init__(self, display):
        """ Ascii Adaptor class takes the display object and convert it into an 
        ascii display.
        """
        self.display = display
        self._grid = NeoPixel(Pin(5), self.display.width * self.display.height)

    def show(self, delta):
        """ Show function will show the ascii display using the given display 
        object. Is used every loop in Controller.

        :param display: Instance that will be converted
        :type display: Display
        :param delta: The amount of time that has passed since the start of the 
        loop in the controller
        :type delta: Number
        """
        pixels = self.display.get_pixels()
        for y in pixels:
            for x in y:
                index = x_y_to_series_conversion(self.display.width, y.index(x), pixels.index(y))
                self._grid[index] = get_color(pixels[y[x]])
        self._grid.write()
