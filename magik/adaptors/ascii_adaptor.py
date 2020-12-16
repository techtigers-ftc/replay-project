from ..utils.styles import Colors
try:
    from os import system
except:
    from utils.system_shim import system

colors = Colors()
def get_color(rgb):
    """ This function will take a rgb tuple, and convert it into a color

    :param rgb: The rgb value that the function uses
    :type rgb: Tuple
    """
    (r, g, b) = rgb
    if r == 1:
        return "{} 0 {}".format(colors.COL_RED, colors.COL_NORMAL)
    elif g == 1:
        return "{} 0 {}".format(colors.COL_LIGHT_GREEN, colors.COL_NORMAL)
    elif b == 1:
        return "{} 0 {}".format(colors.COL_BLUE, colors.COL_NORMAL)
    else:
        return "{} 0 {}".format(colors.COL_BLACK, colors.COL_NORMAL)


class AsciiAdaptor:
    def __init__(self, display):
        """ Ascii Adaptor class takes the display object and convert it into an ascii 
        display.
        """
        self.frame_number = 0
        self.display = display

    def show(self, delta):
        """ Show function will show the ascii display using the given display 
        object. Is used every loop in Controller.

        :param display: Instance that will be converted
        :type display: Display
        :param delta: The amount of time that has passed since the start of the 
        loop in the controller
        :type delta: Number
        """
        system("clear")
        print("Frame: #{}\n".format(self.frame_number))
        self.frame_number += 1
        for row in self.display.get_pixels():
            for pixel in row:
                color = get_color(pixel)
                print(color, end="")
            print("\n")


