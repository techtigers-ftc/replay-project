# This is an example of a game program. You will need a setup and a loop function.
import time 

class Game:
    def __init__(self):
        self.counter = 0
        self.timer = 0
        self.clock = time.time()

    def setup(self, display):
        """ Setup function that is executed before the game loop starts. Can be used
        to initialize variables and other game parameters.

        :param display: Instance of the display class used throughout the game
        :type display: Display
        """
        display.set_pixel(0,0,(1,0,0))
        display.clear_screen()

    def loop1(self, display, delta, inputs):
        """ Loop function will loop throughout the controller program forever. It can 
        be used as the basis for your game

        :param display: Instance that will be converted
        :type display: Display
        :param delta: The amount of time that has passed since the start of the loop 
            in the controller
        :type delta: Number
        """
        display.set_pixel(self.counter, self.counter, (0,1,0))
        diff = time.time() - self.clock
        if diff > 2:
            self.counter += 1
            self.clock = time.time()
        if self.counter == display.width:
            self.counter = 0
            display.clear_screen()

    def loop(self, display, delta, inputs):
        for x in range(0, inputs.x_length):
            for y in range(0, inputs.y_length):
                display.set_pixel(x, y, (inputs.input_value(x, y), 0, 0))
