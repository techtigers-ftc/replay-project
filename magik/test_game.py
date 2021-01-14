""" Module for TestGame class """

import time
from magik import Game

class TestGame(Game):
    """ Example game class that can be used to test displays and inputs
    """
    def __init__(self):
        super().__init__("Testarooni")
        self._counter = 0
        self._prev_time = time.time()
        self._width = 8
        self._height = 8

    def setup(self):
        """ Setup function that is executed before the game loop starts. Can be used
        to initialize variables and other game parameters.
        """
        self._set_display_dimensions(self._width, self._height)
        self._set_input_dimensions(1, 1)
        self._prev_time = time.time()

    def loop(self, input_data, display_data, delta):
        """ Loop function will loop throughout the controller program forever. It can
        be used as the basis for your game

        :param display_data: Instance that will be converted
        :type display_data: display_data
        :param delta: The amount of time that has passed since the start of the loop
            in the controller
        :type delta: Number
        """

        if self._counter == 0:
            display_data.clear_screen()

        if time.time() - self._prev_time > 2:
            self._prev_time = time.time()
            self._counter = (self._counter + 1) % self._width

        display_data.set_pixel(self._counter, self._counter, (1, 0, 0))

        return True

    def loop1(self, input_data, display_data, delta):
        """ Loop function will loop throughout the controller program forever. It can
        be used as the basis for your game

        :param display_data: Instance that will be converted
        :type display_data: display_data
        :param delta: The amount of time that has passed since the start of the loop
            in the controller
        :type delta: Number
        """
        for x_coord in range(0, input_data.width):
            for y_coord in range(0, input_data.height):
                pixel_value = input_data.get_input(x_coord, y_coord)
                display_data.set_pixel(x_coord, y_coord, (pixel_value, 0, 0))
        return True
