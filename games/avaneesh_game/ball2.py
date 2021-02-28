from magik import Sprite
import time

class Ball2(Sprite):
    def __init__(self, x = 0, y=0):
        super().__init__(x,y)
        
    def update(self, input_data):
        if self.has_timer_expired(500):
            self.move(1, 1)
        if self.y == 9:
            self.set_position(0, 0)
            self.move(4,1)
        
            


    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, (255, 255, 255))
        display_data.set_pixel(self.x+1, self.y, (255, 255, 255))
        display_data.set_pixel(self.x+1, self.y+1, (255, 255, 255))
        display_data.set_pixel(self.x, self.y+1, (255, 255, 255))
       