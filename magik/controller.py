#! /usr/bin/python3
import time 
from .ascii_adaptor import AsciiAdaptor
from .turtle_adaptor import TurtleAdaptor
from .np_adaptor import NeoPixelAdaptor
from .display import Display
from .game import Game


class Controller:
    def __init__(self, game, width, height, display_type = "ascii"):
        """ Is a external class that runs the Setup and loop funcions from the game

        :param game: game class
        :type game: object
        :param display_type:
        :type display_type: string
        """
        self.display_type = display_type
        self.game = Game()
        self.width = width
        self.height = height

    def start(self):
        """ runs the setup then loop in a forever loop and keeps track of time
        """
        display = Display(self.width, self.height)
        if self.display_type == "ascii":
            adaptor = AsciiAdaptor(display)
        elif self.display_type =="turtle":
            adaptor = TurtleAdaptor(display)
        elif self.display_type == "np":
            adaptor = NeoPixelAdaptor(display)
        else:
            raise Exception("Invalid display type {}. Please put in valid display type(ascii, turtle, np)".format(self.display_type))
        
        self.game.setup(display)
        clock = time.time()
        while True:
            time.sleep(1)
            delta = time.time() - clock
            clock = time.time()
            self.game.loop(display, delta)
            adaptor.show(delta)

