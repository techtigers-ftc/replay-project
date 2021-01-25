from magik.base_sprite_class import BaseSpriteClass
import time
import random

class FirstSprite(BaseSpriteClass):
    def __init__(self):
        super().__init__()
        self._counter = 0
        self._prev_time = time.time()
        self._width = 3
        self._height = 3
        self._x = 0
        self._y = 0
        self._on = False
        # self._r = random.randrange(65)
        # self._g = random.randrange(65)
        # self._b = random.randrange(65)
        self._colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        self._color = (random.choice(self._colors))
        self.deleted = False
        self._game = 0
        self.bounding_box = 0

    def update(self, input_data):
        # if time.time() - self._prev_time > 1:
        #     self._prev_time = time.time()
        #     self._x = self._counter
        #     self._y = self._counter
        #     self._color = (random.choice(self._colors))
        #     self._counter += 1
        #     self._on = True
        #     child_sprite = FirstSprite()
        #     self._game.add_sprite(child_sprite)
        # else:
        #     self._on = False

        super().update(input_data)
        child_sprite = FirstSprite()
        self._game.add_sprite(child_sprite)
        self._game.remove_sprite(child_sprite)

    def draw(self, display_data):
        if self._on == True:
            display_data.set_pixel(self.x, self.y, self._color)

    def set_game(self, game):
        self._game = game

