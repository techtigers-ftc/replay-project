from magik import Sprite

class Tile(Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self._off_colors = [
            (2, 0, 1),
            (4, 0, 2),
            (8, 0, 4),
            (16, 0, 8),
            (32, 0, 16),
            (64, 0, 32),
            (128, 0, 64),
            (255, 0, 128),
        ]
        self._on_colors = [
            (0, 1, 2),
            (0, 2, 4),
            (0, 4, 8),
            (0, 8, 16),
            (0, 16, 32),
            (0, 32, 64),
            (0, 64, 128),
            (0, 128, 255),
        ]
        self._colors = self._off_colors
        self.x_index = 0

    def update(self, input_data):
        if self.has_timer_expired(250):
            self.x_index += 1
            if input_data.get_input(0,0) == 1 \
                    or input_data.get_input(0,1) == 1 \
                    or input_data.get_input(1,0) == 1 \
                    or input_data.get_input(1,1) == 1:
                self._colors = self._on_colors
            else:
                self._colors = self._off_colors

    def draw(self, display_data):
        for col in range(8):
            # color_index = (self.x_index + x) % 8
            # color = self._colors[color_index]
            for row in range(col+1):
                display_data.set_pixel(x, y, color)











