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

        self._state = "blank"
        if self.has_timer_expired(500):
            self._state = "red"
        if self.has_timer_expired(1000):
            self._state = "yellow"
        if self.has_timer_expired(1500):
            self._state = "green"


    def draw(self, display_data):
        for dx in range(8):
            for dy in range(8):
                display_data.set_pixel(self.x + dx, self.y + dy,
                        self._colors[self._state])

