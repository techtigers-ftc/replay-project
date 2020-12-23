#! /usr/bin/python3
import time 


class Controller:
    def __init__(self, game, display, adaptor, inputs, input_adaptor):
        """ Is a external class that runs the Setup and loop funcions from the game

        :param game: game class
        :type game: object
        :param display_type:
        :type display_type: string
        """
        self.adaptor = adaptor
        self.game = game
        self.display = display
        self.inputs = inputs
        self.input_adaptor = input_adaptor

    def start(self):
        """ runs the setup then loop in a forever loop and keeps track of time
        """
        self.game.setup(self.display)
        clock = time.time()
        while True:
            time.sleep(1)
            delta = time.time() - clock
            clock = time.time()
            self.input_adaptor.read_raw_input()
            self.game.loop(self.display, delta, self.inputs)
            self.adaptor.show(delta)

