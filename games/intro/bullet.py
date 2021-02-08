from magik import Sprite
import time

MIN_X = 0
MIN_Y = 0
MAX_X = 7
MAX_Y = 7

class Bullet(Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__(x,y)
        self._dx = dx
        self._dy = dy
        self._colors = [(32, 0, 16), (16, 32, 0), (0, 16, 32)]
        self._color_index = 0
        self._color = self._colors[0]

    def update(self, input_data):
        if self.has_timer_expired(100):
            self.set_position(self.x + self._dx, self.y + self._dy)
            self._color_index = (self._color_index + 1) % len(self._colors)

        if self._x < MIN_X or self._x > MAX_X \
                or self._y < MIN_Y or self._y > MAX_Y:
            self.destroy()

        self._color = self._colors[self._color_index]

    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, self._color)

