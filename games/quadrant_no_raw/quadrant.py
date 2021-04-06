from magik import Sprite

class Quadrant(Sprite):
    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        super().__init__(x, y)
        self._color = (0, 0, 0)

    def update(self, input_data):

        if input_data.get_input(0, 0) == 1:
            self.set_position(0,0)
            self._color = (255, 0, 0)

        elif input_data.get_input(1, 0) == 1:
            self.set_position(0, 0)
            self._color = (0, 255, 0)

        elif input_data.get_input(0, 1) == 1:
            self.set_position(0, 0)
            self._color = (0, 0, 255)

        elif input_data.get_input(1, 1) == 1:
            self.set_position(0, 0)
            self._color = (128, 128, 0)

        else:
            self._color = (0, 0, 0)


    def draw(self, display_data):
        for dx in range(8):
            for dy in range(8):
                display_data.set_pixel(self.x + dx, self.y + dy, self._color)
