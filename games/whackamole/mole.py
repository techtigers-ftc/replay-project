from magik import Sprite
import random
class Mole(Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.realx = self.x
        self.realy = self.y

    def update(self, input_data):
        print(self.realx,self.realy)
        if self.has_timer_expired(1000) and input_data.get_input(self.realx,self.realy) == 1:
            self.realx= int(random.randint(0,2))
            self.realy= int(random.randint(0,2))
            self.set_position(self.realx,self.y)

    def draw(self, display_data):
         display_data.set_pixel(self.realx, self.realy, (0,0,32))
        

