from magik import Sprite

class Demo(Sprite):
    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        super().__init__(x, y)
        self._color = (0, 0, 0)

    def update(self, input_data):
        if self.has_timer_expired(100):
            if input_data.get_input(0,0) == 1 or input_data.get_input(0,1) == 1 or input_data.get_input(1,0) == 1 or input_data.get_input(1,1) == 1:






    def draw(self, display_data):
        display_data.set_pixel(2,2,(0,1,0))
        display_data.set_pixel(5,6,(0,1,0))
        display_data.set_pixel(2,7,(0,1,0))
        display_data.set_pixel(7,4,(0,1,0))
        display_data.set_pixel(3,2,(0,1,0))
        display_data.set_pixel(6,8,(0,1,0))
        display_data.set_pixel(4,7,(0,1,0))
            



