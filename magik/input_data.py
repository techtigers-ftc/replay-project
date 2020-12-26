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
        self._width = width
        self._height = height
        self._inputs = []
        self._reference = []

        for _ in range(self._height):
            self._inputs.append([0] * self._width)
            self._reference.append([0] * self._width)

    def clear(self):
        """ Clears reference input values
        """
        for x_coord in range(0, self._height):
            for y_coord in range(self._width):
                self._reference[x_coord][y_coord] = 0

    def set_reference(self):
        """ Sets reference input values to actual input values
        """
        for y_coord in range(len(self._inputs)):
            for x_coord in range(len(self._inputs)):
                self._reference[y_coord][x_coord] = \
                        self._inputs[y_coord][x_coord]
        self._reference = self._inputs

    def get_input(self, x_coord, y_coord):
        """ Returns input value of specific coordinate

        :param x_coord: The x coordinate of the input
        :type x_coord: Number
        :param y_coord: The y coordinate of the input
        :type y_coord: Number
        """

        return self._inputs[x_coord][y_coord] - self._reference[x_coord][y_coord]

    def set_input(self, x_coord, y_coord, value):
        """ Sets an input value at specific coordinates

        :param x_coord: The x coordinate of the input
        :type x_coord: Number
        :param y_coord: The y coordinate of the input
        :type y_coord: Number
        """

        if x_coord < 0 or x_coord >= self._width:
            raise ValueError("X coordinate is out of range")

        if y_coord < 0 or y_coord >= self._height:
            raise ValueError("Y coordinate is out of range")

        self._inputs[x_coord][y_coord] = value

    def dump_input(self):
        """ Debug method for dumping all input values
        """

        values = self._inputs
        for row in values:
            for input_value in row:
                print(input_value, end="")
            print("")

    def dump_reference(self):
        """ Debug method for dumping all reference values
        """

        values = self._reference
        for row in values:
            for input_value in row:
                print(input_value, end="")
            print("")

    @property
    def width(self):
        """ Read only property of width.

        :return: Returns width of input array
        :type return: Number
        """

        return self._width

    @property
    def height(self):
        """ Read only property of height.

        :return: Returns height of input array
        :type return: Number
        """

        return self._height
