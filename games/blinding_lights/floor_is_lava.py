from magik import Sprite
import time


class Lava(Sprite):
    def __init__(self, x):
        super().__init__()
        self._width = 8
        self._height = 1
        self.counter = self.width
        self.prev_time = time.time()
        self._x = x


    def update(self, input_data):
        if time.time() - self.prev_time > 1.5:
            self.counter = self.counter - 1
            self.prev_time = time.time()

            


    def draw(self, display_data):
        for y in range(0,self.counter):

            display_data.set_pixel(self._x,y,(1,0,0))
            display_data.set_pixel(2,2,(0,1,0))
            display_data.set_pixel(5,6,(0,1,0))
            display_data.set_pixel(2,7,(0,1,0))
            display_data.set_pixel(7,4,(0,1,0))
            display_data.set_pixel(3,2,(0,1,0))
            display_data.set_pixel(6,8,(0,1,0))
            display_data.set_pixel(4,7,(0,1,0))
            

        






