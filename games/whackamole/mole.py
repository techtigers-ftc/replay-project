from magik import Sprite
import random
from games.whackamole.success import Success
from games.whackamole.fail import Fail

class Mole(Sprite):
    def __init__(self, score=0):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        super().__init__(x, y)
        self._mole_states = [
            # [ (1, 0), (0, 1), (2, 1), (1, 2) ],
            # [ (0, 0), (0, 2), (2, 0), (2, 2) ]
            # [ (0,0), (1, 0), (2, 0) ],
            # [ (0,0), (1, 0), (2, 0), (0,1), (1, 1), (2, 1) ],
            [ (0,0), (1, 0), (2, 0), (0,1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2) ],
        ]
        self._mole_colors = [
            (4, 8, 0),
            (8, 16, 0),
            (16, 32, 0),
            (32, 64, 0),
            (64, 128, 0),
            (128, 255, 0),
            (0, 4, 8),
            (0, 8, 16),
            (0, 16, 32),
            (0, 32, 64),
            (0, 64, 128),
            (0, 128, 255),
            (4, 0, 8),
            (8, 0, 16),
            (16, 0, 32),
            (32, 0, 64),
            (64, 0, 128),
            (128, 0, 255),
        ]
        self._state_index = 0
        self._color_index = 0
        self.score = 0

    def update(self, input_data):
        if input_data.get_input(0,0) == 1 \
            or input_data.get_input(0,1) == 1 \
            or input_data.get_input(1,0) == 1 \
            or input_data.get_input(1,1) == 1:
                self._game.add_sprite(Success())
                self._game.add_sprite(Mole())
                self.destroy()
                 
        if self.has_timer_expired(100, False):
            self._color_index = (self._color_index + 1) % len(self._mole_colors)

        if self.has_timer_expired(1800):
            self._state_index += 1
            if self._state_index == len(self._mole_states):
                self._game.add_sprite(Fail()) 
                self._game.add_sprite(Mole())
                self.destroy()



    def draw(self, display_data):
        
        deltas = self._mole_states[self._state_index]
        color = self._mole_colors[self._color_index]
        for index in range(len(deltas)):
            dx, dy = deltas[index]
            display_data.set_pixel(self.x + dx, self.y + dy, color)









