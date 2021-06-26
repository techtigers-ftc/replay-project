from magik import Sprite
from games.plank.pressure import Pressure

class Sensor(Sprite):
    def __init__(self, x, y, plank_state, position):
        super().__init__(x, y)
        self._color = (64, 64, 0)
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

        print(input_area)
        if input_area > 400:
            self._game.add_sprite(Pressure(self.x, self.y, self.plank_state, 
                self.position))
            self.destroy()

    def draw(self, display_data):
        for diff in range(6):
            display_data.set_pixel(self.x + 1 + diff, self.y + 1 + diff, 
                    self._color)
        for diff in range(6):
            display_data.set_pixel(self.x + 1 + diff, self.y + 6 - diff, 
                    self._color)

