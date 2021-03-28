from magik import Sprite

class Quadrant(Sprite):
    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        super().__init__(x, y)
        self._color = (0, 0, 0)

    def update(self, input_data):
        a = input_data.get_input(0,0)

        b = input_data.get_input(0,1)

        c = input_data.get_input(1,0)

        d = input_data.get_input(1,1)

        if self.has_timer_expired(100):
            red = (a-300)/10
            green = (b-300)/10
            blue = (c-300)/10

            if red > 255:
                red = 255
            if green > 255:
                green = 255
            if blue > 255:
                blue = 255


            if red < 0:
                red = 0
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0

            red = round(red)
            blue = round(blue)
            green = round(green)


            print(a,b,c)
            self.set_position(0,0)
            self._color = (red, green, 0)


    def draw(self, display_data):
        if self._color == (0, 0, 0):
            return
        for dx in range(8):
            for dy in range(8):
                display_data.set_pixel(self.x + dx, self.y + dy, self._color)

