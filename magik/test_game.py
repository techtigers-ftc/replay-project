""" Module for TestGame class """

import time
from magik import Game

class TestGame(Game):
    """ Example game class that can be used to test displays and inputs
    """
    def __init__(self):
        super().__init__("Testarooni")
        self.counter = 0
        self.timer = 0
        self.clock = time.time()

    def setup(self):
        """ Setup function that is executed before the game loop starts. Can be used
        to initialize variables and other game parameters.
        """
        self._set_display_dimensions(5, 5)
        self._set_input_dimensions(5, 5)

    def loop(self, input_data, display_data, delta):
        """ Loop function will loop throughout the controller program forever. It can
        be used as the basis for your game

        :param display_data: Instance that will be converted
        :type display_data: display_data
        :param delta: The amount of time that has passed since the start of the loop
            in the controller
        :type delta: Number
        """
        display_data.set_pixel(0, 0, (1, 0, 0))

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
