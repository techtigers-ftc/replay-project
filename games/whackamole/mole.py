from magik import Sprite
import random
from games.whackamole.success import Success
from games.whackamole.fail import Fail

class Mole(Sprite):
    """ Whackamole sprite class that allows the mole to move around and get whacked
    """
    def __init__(self):
        """ Innitializes the variables and params
        """
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        super().__init__(x, y)

        self._display_states = [
            # [ (1, 0), (0, 1), (2, 1), (1, 2) ],
            # [ (0, 0), (0, 2), (2, 0), (2, 2) ]
            # [ (0,0), (1, 0), (2, 0) ],
            # [ (0,0), (1, 0), (2, 0), (0,1), (1, 1), (2, 1) ],
            [ (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (2, 1), (0, 2), (1, 2), (2, 2) ],
        ]
        self._colors = [
            (128, 0, 255)
        ]
        self._display_state_index = 0
        self._color_index = 0
        self._ticks = 0
        self._state = None

    def update(self, input_data):
        """ Is called every cycle and updates the position or state of the mole in game.

        :param input_data: instance of input data class
        :type input_data: InputData
        """
        if not self.has_timer_expired(100):
            return

        self._ticks += 1
        input_detected = input_data.get_input(0,0) == 1 \
                            or input_data.get_input(0,1) == 1 \
                            or input_data.get_input(1,0) == 1 \
                            or input_data.get_input(1,1) == 1
        print(input_data.get_input(0,0),
                input_data.get_input(1,0),
                input_data.get_input(0,1),
                input_data.get_input(1,1))
        if self._state is not None:
            if self._ticks > 5:
                self._game.add_sprite(Mole())
                self.destroy()
        elif self._ticks >= 20:
            self._state= "FAIL"
            self._ticks = 0
            
        elif input_detected:
            self._state = "SUCCESS"
            self._ticks = 0

        else:
            self._color_index = (self._color_index + 1) % len(self._colors)
            self._display_state_index = (self._display_state_index + 1) % \
                                                    len(self._display_states)


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









