

from magik import Sprite
import random

class Success(Sprite):
    def __init__(self, score=0):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        super().__init__(x, y)

    def update(self, input_data):
        pass 


    def draw(self, display_data):
            display_data.set_pixel(0,7 , (0,0,255))
            display_data.set_pixel(1,7 , (0,0,255))
            display_data.set_pixel(0,6 , (0,0,255))
            display_data.set_pixel(1,6 , (0,0,255))
            self.destroy()









