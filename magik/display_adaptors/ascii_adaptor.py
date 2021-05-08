""" Module for AsciiAdaptor """

from .base_display_adaptor import BaseDisplayAdaptor
from ..utils.styles import Colors
import time

try:
    from os import system
except: # pylint:disable=bare-except
    from utils.system_shim import system

from ..utils import system_check

CLEAR_SCREEN_COMMAND = "cls" if system_check.system_check() == "windows" \
                             else "clear"

colors = Colors()
def get_color_ascii(rgb):
    """ This function will take a rgb tuple, and convert it into a color

    :param rgb: The rgb value that the function uses
    :type rgb: Tuple
    """
    (red, green, blue) = rgb
    led_char = "\u29BF"

    if red >= 1:
        if blue >= 1:
            if green >= 1:
                return "{} {} {}".format(colors.COL_WHITE, led_char, colors.COL_NORMAL)
            return "{} {} {}".format(colors.COL_PURPLE, led_char, colors.COL_NORMAL)
        if green >= 1:
            return "{} {} {}".format(colors.COL_YELLOW, led_char, colors.COL_NORMAL)
        return "{} {} {}".format(colors.COL_RED, led_char, colors.COL_NORMAL)

    if green >= 1:
        if blue >= 1:
            return "{} {} {}".format(colors.COL_LIGHT_CYAN, led_char, colors.COL_NORMAL)
        return "{} {} {}".format(colors.COL_LIGHT_GREEN, led_char, colors.COL_NORMAL)

    if blue >= 1:
        return "{} {} {}".format(colors.COL_BLUE, led_char, colors.COL_NORMAL)

    return "{} {} {}".format(colors.COL_BLACK, led_char, colors.COL_NORMAL)

class AsciiAdaptor(BaseDisplayAdaptor): # pylint:disable=too-few-public-methods
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

        # Display Data gives it to you in a 2-dimensional array in form x,y, and
        # we want the number of lines, for which we need the y-coordinate
        lines = ['|'] * len(display_data.pixels[0])

        for x_index in range(display_data.width):
            for y_index in range(display_data.height):
                line_index = display_data.height - y_index - 1
                pixel = display_data.pixels[x_index][y_index]

                color = get_color_ascii(pixel)
                lines[line_index] += color

        for line_index in range(len(lines)):
            lines[line_index] += '|'

        self._frame_number += 1
        system(CLEAR_SCREEN_COMMAND)
        print("Frame: #{}\n".format(self._frame_number))
        print('\n'.join(lines))
