from magik import Sprite
import random
class Mole(Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)

    def update(self, input_data):
        if self.has_timer_expired(1000):
            self.set_position(random.randint(0,8),random.randint(0,8))

    def draw(self, display_data):
         display_data.set_pixel(self.x, self.y, (0,0,32))
        

