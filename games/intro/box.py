from magik import Sprite

from bullet import Bullet

class Box(Sprite):
    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        super().__init__(x, y)
        self._colors = [(32, 0, 0), (0, 32, 0), (0, 0, 32)]
        self._color_index = 0
        self._color = self._colors[0]
        self._counter = 0
        self._dx = dx
        self._dy = dy

    def update(self, input_data):
        if self.has_timer_expired(500):
            self._color_index = (self._color_index + 1) % len(self._colors)
            self._counter += 1
            # self.set_position(self.x + self._dx, self.y + self._dy)

        self._color = self._colors[self._color_index]

        if self._counter > 20:
            self.destroy()

        if self._counter % 3 == 0:
            self._game.add_sprite(Bullet(self.x, self.y, -1, 0))
            self._game.add_sprite(Bullet(self.x, self.y, 0, -1))
            self._game.add_sprite(Bullet(self.x, self.y, -1, -1))

            self._game.add_sprite(Bullet(self.x, self.y + 1, -1, 0))
            self._game.add_sprite(Bullet(self.x, self.y + 1, 0, 1))
            self._game.add_sprite(Bullet(self.x, self.y + 1, -1, 1))

            self._game.add_sprite(Bullet(self.x + 1, self.y, 1, 0))
            self._game.add_sprite(Bullet(self.x + 1, self.y, 0, -1))
            self._game.add_sprite(Bullet(self.x + 1, self.y, 1, -1))

            self._game.add_sprite(Bullet(self.x + 1, self.y + 1, 1, 0))
            self._game.add_sprite(Bullet(self.x + 1, self.y + 1, 0, 1))
            self._game.add_sprite(Bullet(self.x + 1, self.y + 1, 1, 1))

    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, self._color)
        display_data.set_pixel(self.x + 1, self.y, self._color)
        display_data.set_pixel(self.x, self.y + 1, self._color)
        display_data.set_pixel(self.x + 1, self.y + 1, self._color)


