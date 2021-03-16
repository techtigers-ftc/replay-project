from magik import Sprite
import random
from games.whackamole.success import Success
from games.whackamole.fail import Fail

class Mole(Sprite):
    def __init__(self):
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

    def update(self, input_data):
        if not self.has_timer_expired(100):
            return

        self._ticks += 1
        input_detected = input_data.get_input(0,0) == 1 \
                            or input_data.get_input(0,1) == 1 \
                            or input_data.get_input(1,0) == 1 \
                            or input_data.get_input(1,1) == 1

        if self._ticks >= 20:
            self._game.add_sprite(Fail())
            self._game.add_sprite(Mole())
            self.destroy()
        elif input_detected:
            self._game.add_sprite(Success())
            self._game.add_sprite(Mole())
            self.destroy()
        else:
            self._color_index = (self._color_index + 1) % len(self._colors)
            self._display_state_index = (self._display_state_index + 1) % \
                                                    len(self._display_states)

    def draw(self, display_data):
        deltas = self._display_states[self._display_state_index]
        color = self._colors[self._color_index]
        for index in range(len(deltas)):
            dx, dy = deltas[index]
            display_data.set_pixel(self.x + dx, self.y + dy, color)









