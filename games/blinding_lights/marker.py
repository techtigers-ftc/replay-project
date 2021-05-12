from magik import Sprite
import time

class Marker(Sprite):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._alpha = 3
        self.prev_time = time.time()

    def update(self, input_data):
        if time.time() - self.prev_time > 1.5:
            self.prev_time = time.time()


    def draw(self, display_data):
        for a in range(self._alpha):
            display_data.set_pixel(self._x + a, self._y, (1,0,0) )
            display_data.set_pixel(self._x - a, self._y, (0,0,1) )
            display_data.set_pixel(self._x, self._y + a, (0,1,0) )
            display_data.set_pixel(self._x, self._y - a, (0,1,1) )
