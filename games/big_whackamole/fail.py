from magik import Sprite
import random

class Fail(Sprite):

    def __init__(self, score=0):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        super().__init__(x, y)

    def update(self, input_data):
        pass



    def draw(self, display_data):
            display_data.set_pixel(0,7 , (255,0,0))
            display_data.set_pixel(1,7 , (255,0,0))
            display_data.set_pixel(0,6 , (255,0,0))
            display_data.set_pixel(1,6 , (255,0,0))
            self.destroy()
