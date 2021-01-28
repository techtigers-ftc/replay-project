from magik import Sprite
import time

from bullet import Bullet

class SpaceShip(Sprite):
    def __init__(self, x = 4, y = 4):
        super().__init__(x, y)
        self._prev_time = time.time()
        self._colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        self._color_index = 0
        self._color = self._colors[0]
        self._counter = 0

    def update(self, input_data):
        if time.time() - self._prev_time > 1:
            self._color_index = (self._color_index + 1) % len(self._colors)
            self._prev_time = time.time()
            self._counter += 1

        self._color = self._colors[self._color_index]

        if self._counter > 20:
            self.destroy()

        if input_data.get_input(0, 0) == 1:
            self._game.add_sprite(Bullet(self.x + 1, self.y, 1, 0))
            self._game.add_sprite(Bullet(self.x - 1, self.y, -1, 0))
            self._game.add_sprite(Bullet(self.x, self.y + 1, 0, 1))
            self._game.add_sprite(Bullet(self.x, self.y - 1, 0, -1))

            self._game.add_sprite(Bullet(self.x + 1, self.y + 1, 1, 1))
            self._game.add_sprite(Bullet(self.x - 1, self.y + 1, -1, 1))
            self._game.add_sprite(Bullet(self.x + 1, self.y - 1, 1, -1))
            self._game.add_sprite(Bullet(self.x - 1, self.y - 1, -1, -1))

    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, self._color)


