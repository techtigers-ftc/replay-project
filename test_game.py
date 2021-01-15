""" Module for TestGame class """

import time
import random
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
        self._x = random.randrange(self._width)
        self._y = random.randrange(self._height)
        self._r = random.randrange(65)
        self._g = random.randrange(65)
        self._b = random.randrange(65)
        self._color = (self._r, self._g, self._b)

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

        if time.time() - self._prev_time > 0.5:
            self._prev_time = time.time()
            self._x = random.randrange(self._width)
            self._y = random.randrange(self._height)
            self._r = random.randrange(65)
            self._g = random.randrange(65)
            self._b = random.randrange(65)
            self._color = (self._r, self._g, self._b)
            display_data.clear_screen()


        display_data.set_pixel(self._x, self._y, self._color)

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
