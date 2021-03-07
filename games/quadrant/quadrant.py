from magik import Sprite

class Quadrant(Sprite):
    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        super().__init__(x, y)
        self._color = (0, 0, 0)

    def update(self, input_data):
        if self.has_timer_expired(100):
            if input_data.get_input(0, 0) == 1:
                self.set_position(0,0)
                self._color = (16, 0, 0)
            elif input_data.get_input(1, 0) == 1:
                self.set_position(0, 4)
                self._color = (0, 16, 0)
            elif input_data.get_input(0, 1) == 1:
                self.set_position(4, 0)
                self._color = (0, 0, 16)
            elif input_data.get_input(1, 1) == 1:
                self.set_position(4, 4)
                self._color = (8, 8, 0)
            else:
                self._color = (0, 0, 0)


    def draw(self, display_data):
        if self._color == (0, 0, 0):
            return
        for dx in range(4):
            for dy in range(4):
                display_data.set_pixel(self.x + dx, self.y + dy, self._color)

