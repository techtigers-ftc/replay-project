""" Module for the Controller class """
import time
from .display_adaptors import BaseDisplayAdaptor
from .input_adaptors import BaseInputAdaptor
from .game import Game


class Controller:
    """ Controlls all of the elements that make up the game. Allows user to
    configure the input and outputs and game logic and lets the user run their
    game."""

    def __init__(self):
        """ Creates a new instance of controller class. Controller needs to be
        configured before it can be run
        """

        self._display_adaptor = None
        self._game = None
        self. _input_adaptor = None
        self._frame_delay = 0

    def set_display_adaptor(self, display_adaptor):
        """ Sets the display adaptor for the game

        :param display_adaptor: Instance of adaptor to render the game
        :type display_adaptor: DisplayAdapter
        """

        if not isinstance(display_adaptor, BaseDisplayAdaptor):
            raise TypeError("Invalid display adaptor")

        self._display_adaptor = display_adaptor

    def set_game(self, game):
        """ Sets the game logic

        :param game: Instance of the game logic
        :type Game: GameAdaptor
        """

        if not isinstance(game, Game):
            raise TypeError("Invalid game")
        self._game = game

    def set_input_adaptor(self, input_adaptor):
        """ Sets the input adaptor for the game

        :param input_adaptor: Instance of input adapter
        :type input_adaptor: BaseInputAdaptor
        """

        if not isinstance(input_adaptor, BaseInputAdaptor):
            raise TypeError("Invalid input adaptor")
        self._input_adaptor = input_adaptor

    def set_frame_rate(self, frame_rate):
        """ Sets the frame rate for the game

        :param frame_rate: The rate the frame resets at
        :type Input: Number
        """

        if not isinstance(frame_rate, int) and not isinstance(frame_rate, float):
            raise TypeError("Invalid frame rate")

        if frame_rate < 0:
            raise ValueError("Frame rate cannot be negative")

        self._frame_delay = 1/frame_rate

    def start(self):
        """ Sets up and starts the game loop
        """

        if not isinstance(self._display_adaptor, BaseDisplayAdaptor):
            raise Exception("Display adaptor has not been set")

        if not isinstance(self._game, Game):
            raise Exception("Game has not been set")

        if not isinstance(self._input_adaptor, BaseInputAdaptor):
            raise Exception("Input adaptor has not been set")

        # Setting up the game, inputs and outputs
        self._game.setup()
        display_data = self._game.create_display()
        input_data = self._game.create_input()

        clock = time.time()
        running = True
        while running:
            delta = time.time() - clock
            clock = time.time()
            time.sleep(max(self._frame_delay - delta, 0))

            self._input_adaptor.read(delta, input_data)

            running = self._game.loop(input_data, display_data, delta)
            self._display_adaptor.show(delta, display_data)

