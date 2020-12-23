""" Module for InputData class """

class InputData:
    """ Abstract representation of the inputs from the physical devices
    """
    def __init__(self, width, height):
        """ Initialize class instance

        :param width: The width of the row of inputs
        :type width: Number
        :param length: The length of the column of inputs
        :type length: Number
        """
        self.width = width
        self.height = height
        self.inputs = []
        self.reference = []

        for _ in range(self.height):
            self.inputs.append([0] * self.width)
            self.reference.append([0] * self.width)

    def clear(self):
        """ Clears reference input values
        """
        for x_coord in range(0, self.height):
            for y_coord in range(self.width):
                self.reference[x_coord][y_coord] = 0

    def set_reference(self):
        """ Sets reference input values to actual input values
        """
        for y_coord in range(len(self.inputs)):
            for x_coord in range(len(self.inputs)):
                self.reference[y_coord][x_coord] = self.inputs[y_coord][x_coord]
        self.reference = self.inputs

    def get_input(self, x_coord, y_coord):
        """ Returns input value of specific coordinate

        :param x_coord: The x coordinate of the pixel
        :type x_coord: Number
        :param y_coord: The y coordinate of the pixel
        :type y_coord: Number
        :param color: The color to apply to the pixel
        :return: The difference of the current and reference inputs
        :type return: Number
        """

        print(self.inputs, self.reference, x_coord, y_coord)
        return self.inputs[x_coord][y_coord] - self.reference[x_coord][y_coord]
