from magik import Sprite
import random
from games.big_whackamole.success import Success
from games.big_whackamole.fail import Fail

class Mole(Sprite):
    """ Whackamole sprite class that allows the mole to move around and get whacked
    """
    def __init__(self, score):
        """ Innitializes the variables and params
        """
        x = random.randint(0, 13)
        y = random.randint(0, 21)
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
        self._x_input_areas = [ (0, 6), (7, 13) ]
        self._y_input_areas = [ (0, 6), (7, 13), (14, 21) ]
        self.score = score

    def update(self, input_data):
        """ Is called every cycle and updates the position or state of the mole in game.

        :param input_data: instance of input data class
        :type input_data: InputData
        """
        if not self.has_timer_expired(100):
            return

        self._ticks += 1
        
        input_area = 0
        break_loop = False
        for y_input_area in self._y_input_areas:
            if self.y >= y_input_area[0] <= y_input_area[1]:
                for x_input_area in self._x_input_areas:
                    if self.x >= x_input_area[0] <= x_input_area[1]:
                        input_area = (self._x_input_areas.index(x_input_area), 
                                self._y_input_areas.index(y_input_area))
                        break_loop = True
            if break_loop:
                break
                        
        input_detected = input_data.get_input(input_area[0], input_area[1]) == 1\

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
            self.score.add(1)

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
