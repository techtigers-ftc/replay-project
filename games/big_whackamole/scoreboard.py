from magik import Sprite
import random
from games.big_whackamole.success import Success
from games.big_whackamole.fail import Fail

class Scoreboard(Sprite):
    """ Whackamole sprite class that allows the mole to move around and get whacked
    """
    def __init__(self, score):
        """ Innitializes the variables and params
        """
        self.score = score

        numbers = [
                ]

    def update(self, input_data):
        """ Is called every cycle and updates the position or state of the mole in game.

        :param input_data: instance of input data class
        :type input_data: InputData
        """
        if not self.has_timer_expired(100):
            return


    def draw(self, display_data):
        """ Draws the updated sprite on the screen

        :param display_data: Instance of the display data class
        :type display_data: DisplayData
        """

        deltas = self._display_states[self._display_state_index]
        color = self._colors[self._color_index]

        if self._state == "SUCCESS":
            color = (0,255,0)
        elif self._state == "FAIL":
            color = (255,0,0)
        for index in range(len(deltas)):
            dx, dy = deltas[index]
            display_data.set_pixel(self.x + dx, self.y + dy, color)
