from magik.base_sprite_class import BaseSpriteClass
import time
import random

class FirstSprite(BaseSpriteClass):
    def __init__(self):
        super().__init__()
        self._counter = 0
        self._prev_time = time.time()
        self._width = 1
        self._height = 1
        self._x = 0
        self._y = 0
        self._change = False
        # self._r = random.randrange(65)
        # self._g = random.randrange(65)
        # self._b = random.randrange(65)
        self._colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        self._color = (random.choice(self._colors))

    def update(self, input_data):
        if time.time() - self._prev_time > 0.5:
            self._prev_time = time.time()
            self._x = random.randrange(self._width)
            self._y = random.randrange(self._height)
            self._color = (random.choice(self._colors))
            self._change = True

    def draw(self, display_data):
        self._width = display_data.width
        self._height = display_data.height
        if self._change == True:
            self._change = False

        display_data.set_pixel(self._x, self._y, self._color)

