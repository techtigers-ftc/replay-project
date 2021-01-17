""" Module for the game class """

from .display_data import DisplayData
from .input_data import InputData

class Game:
    """ Abstract representation of a game. Contains game logic that can be
    implemented within a game loop
    """

    def __init__(self, sprites):
        """ Initializes the game instance

        :param name: The name of the game
        :type name: str
        """
        if not isinstance(sprites, list):
            raise TypeError("No sprites given in list form")

        self._display_width = 0
        self._display_height = 0

        self._input_width = 0
        self._input_height = 0

        self._sprites = sprites
        print(self._sprites)

    def set_display_dimensions(self, width, height):
        # Sets the display dimensions of the game.

        self._display_width = width
        self._display_height = height
    def set_input_dimensions(self, width, height):

        # Sets the input dimensions of the game.

        self._input_width = width
        self._input_height = height

    def create_display(self):
        """ Create a display data object based on the game's defined dimensions.
        This method expects inheriting classes to set game dimensions using the
        _set_display_dimensions() method.
        """

        return DisplayData(self._display_width, self._display_height)

    def create_input(self):
        """ Create an input data object based on the game's defined dimensions.
        This method expects inheriting classes to set game dimensions using the
        _set_input_dimensions() method.
        """

        return InputData(self._input_width, self._input_height)

    def setup(self): # pylint:disable=no-self-use
        """ Can be implemented by child classes to setup the game """

        self.set_display_dimensions(self._display_width, self._display_height)
        self.set_input_dimensions(1, 1)

    def loop(self, input_data, display_data, delta): # pylint:disable=no-self-use
        """ Can be implemented by child classes to execute the main game logic

        :param input_data: An object containing inputs from the user
        :type input_data: InputData
        :param display_data: An object to write the expected display output to
        :type input_data: DisplayData
        :param delta: The time in milliseconds since this method was called
        :type delta: Number
        """
        display_data.clear_screen()
        for sprite in self._sprites:
            print("Updating {}".format(sprite))
            sprite.update(input_data)
        for sprite in self._sprites:
            print("Drawing {}".format(sprite))
            sprite.draw(display_data)
        return True


