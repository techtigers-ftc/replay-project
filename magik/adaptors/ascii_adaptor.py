""" Module for AsciiAdaptor """

from ..display_adaptor import DisplayAdaptor
from ..utils.styles import Colors
try:
    from os import system
except: # pylint:disable=bare-except
    from utils.system_shim import system

colors = Colors()
def get_color_ascii(rgb):
    """ This function will take a rgb tuple, and convert it into a color

    :param rgb: The rgb value that the function uses
    :type rgb: Tuple
    """
    (red, green, blue) = rgb
    led_char = "\u29BF"

    if red >= 1:
        return "{} {} {}".format(colors.COL_RED, led_char, colors.COL_NORMAL)

    if green >= 1:
        return "{} {} {}".format(colors.COL_LIGHT_GREEN, led_char, colors.COL_NORMAL)

    if blue >= 1:
        return "{} {} {}".format(colors.COL_BLUE, led_char, colors.COL_NORMAL)

    return "{} {} {}".format(colors.COL_BLACK, led_char, colors.COL_NORMAL)

class AsciiAdaptor(DisplayAdaptor): # pylint:disable=too-few-public-methods
    """ Implements a display adaptor that uses ascii characters to show the game
        display.
    """

    def __init__(self):
        super().__init__()
        self._frame_number = 0

    def show(self, delta, display_data):
        """ Show function will show the ascii display using the given display
            object. Is used every loop in Controller.

        :param delta: The amount of time that has passed since the start of the
        loop in the controller
        :type delta: Number
        :param display: Instance that will be converted
        :type display: Display
        """
        system("clear")
        print("Frame: #{}\n".format(self._frame_number))
        self._frame_number += 1
        for row in display_data.pixels:
            for pixel in row:
                color = get_color_ascii(pixel)
                print(color, end="")
            print("")
