from magik import Sprite
import random

class Chair(Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self._colors = [(32, 0, 0), (0, 32, 0), (0, 0, 32)]
        self._color = self._colors[0]
        self._show = False
        self._duration = random.randrange(1000,10000,1)

    def update(self, input_data):
        if self.has_timer_expired(self._duration):
            self._show = True

    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, self._color)


