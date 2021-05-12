from magik import Sprite

class Pressure(Sprite):
    def __init__(self, x, y, plank_state, position):
        super().__init__(x, y)
        self._colors = {
                "red": (64, 0, 0),
                "yellow": (64, 64, 0),
                "green": (0, 64, 0),
                "blue": (0, 0, 64),
                "blank": (0, 0, 0)
                }
        self._state = False
        self.plank_state = plank_state
        self.position = position
        
    def update(self, input_data):
        input_area = 0

        for x_coord in range(input_data.width):
            for y_coord in range(input_data.height):
                if self.x >= x_coord * 8 and self.x < (x_coord + 1) * 8:
                    if self.y >= y_coord * 8 and self.y < (y_coord + 1) * 8:
                        input_area = input_data.get_input(x_coord, y_coord)

        if self.has_timer_expired(100):
            if input_area > 400:
                self.plank_state.set_state(True, self.position)
            else:
                self.plank_state.set_state(False, self.position)


    def draw(self, display_data):
        for dx in range(8):
            for dy in range(8):
                display_data.set_pixel(self.x + dx, self.y + dy,
                        self._colors[self.plank_state.get_state()])

