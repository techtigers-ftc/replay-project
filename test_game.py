# This is an example of a game program. You will need a setup and a loop function.
import time 
from magik import Game

class TestGame(Game):
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
        self._set_input_dimensions(1, 1)

    def loop1(self, input_data, display_data, delta):
        """ Loop function will loop throughout the controller program forever. It can 
        be used as the basis for your game

        :param display_data: Instance that will be converted
        :type display_data: display_data
        :param delta: The amount of time that has passed since the start of the loop 
            in the controller
        :type delta: Number
        """
        display_data.set_pixel(self.counter, self.counter, (0,1,0))
        diff = time.time() - self.clock
        if diff > 2:
            self.counter += 1
            self.clock = time.time()
        if self.counter == display_data.width:
            self.counter = 0
            display_data.clear_screen()

    def loop(self, input_data, display_data, delta):
        for x in range(0, 1):
            for y in range(0, 1):
                display_data.set_pixel(x, y, (input_data.get_input(x, y), 0, 0))
        return True
