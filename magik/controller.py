""" Module for the Controller class """
#! /usr/bin/python3
import time
from .display_adaptor import DisplayAdaptor

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
        self._display = None
        self._input = None
        self. _input_adaptor = None

    def set_display(self, adaptor):
        """Sets the adaptor for the game

        :param adaptor: instance of adaptor to render the game
        :type adaptor: DisplayAdapter
        """
        if not isinstance(adaptor, DisplayAdaptor):
            raise TypeError("Invalid adaptor (arg #1)")

        self._display_adaptor = adaptor

    def set_game(self, game):
        """Sets the game logic

        :param game: instance of the game logic
        :type Game: GameAdaptor 
        """
        if not isinstance(game, GameAdaptor):
            raise TypeError("Invalid game")
        self._game = game

    def set_input(self, inputs):
        """ Sets the input for the game

        :param inputs: instance of input adapter to take unputs
        :type Input:InputAdaptor

        """
        if not isinstance(inputs, InputAdaptor) is None:
            raise ValueError("give valid inputs class")
        self._input = inputs

    def start(self):
        """ runs the setup then loop in a forever loop and keeps track of time
        """
        self._game.setup(self._display)
        clock = time.time()

        while True:
            time.sleep(1)
            delta = time.time() - clock
            clock = time.time()
            self._input_adaptor.read_raw_input()

            # TODO: Accept true/false as a return value from game.loop and use
            # that to stop the controller. This will allow the game to control
            # the execution of the controller
            self._game.loop(self._display, delta, self._input)

            self._display_adaptor.show(delta)
