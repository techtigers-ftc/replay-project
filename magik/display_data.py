""" Module for DisplayData class """

class DisplayData:
    """ Abstract representation of a display that can be used to develop games
    that many different displays can use if paired with the right adapter
    """
    # Init with initial variables
    def __init__(self, width, height):
        """ Initializes class instance

        :param width: how many pixels in one row
        :type width: Number
        :param height: how mnay pixels in one column
        :type height: Number
        """
        self.pixels = []
        self.height = height
        self.width = width

        # Sets the pixels array to all off
        for _ in range(self.height):
            self.pixels.append([(0,0,0)] * self.width)

    def clear_screen(self):
        """Clears the screen and sets all pixels to (0,0,0)
        """

        for x_coord in range(self.height):
            for y_coord in range(self.width):
                self.pixels[x_coord][y_coord] = (0,0,0)

    def set_pixel(self, x_coord, y_coord, color):
        """Sets a certain pixel to a color

        :param x_coord: The x coordinate of the pixel
        :type x_coord: Number
        :param y_coord: The y coordinate of the pixel
        :type y_coord: Number
        :param color: The color to apply to the pixel
        :type color: tuple
        """

        self.pixels[x_coord][y_coord] = color

    @property
    def pixels(self):
        """Returns the pixel grid represented by this object"""

        return self.pixels
