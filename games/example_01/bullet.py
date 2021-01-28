from magik import Sprite
import time

MIN_X = 0
MIN_Y = 0
MAX_X = 8
MAX_Y = 8

class Bullet(Sprite):
    def __init__(self, x, y, dx, dy):
        super().__init__(x,y)
        self._dx = dx
        self._dy = dy
        self._prev_time = time.time()
        self._colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        self._color_index = 0
        self._color = self._colors[0]

    def update(self, input_data):
        if time.time() - self._prev_time > 0.5:
            self._prev_time = time.time()
            self.set_position(self.x + self._dx, self.y + self._dy)
            self._color_index = (self._color_index + 1) % len(self._colors)

        if self._x < MIN_X or self._x > MAX_X \
                or self._y < MIN_Y or self._y > MAX_Y:
            self.destroy()

        self._color = self._colors[self._color_index]

    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, self._color)

