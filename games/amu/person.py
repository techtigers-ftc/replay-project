from magik import Sprite

class Person(Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self.__out = True
        self.__in = False

    def update(self, input_data):
        if self.has_timer_expired(500):
            if self.__out:
                self.__out = False
                self.__in = True
            else:
                self.__out = True
                self.__in = False

    def draw(self, display_data):
        if self.__out:

            display_data.set_pixel(3, 7, (0, 0, 128))
            display_data.set_pixel(4, 7, (0, 0, 128))
            display_data.set_pixel(5, 7, (0, 0, 128))

            display_data.set_pixel(3, 6, (0, 0, 128))
            display_data.set_pixel(5, 6, (0, 0, 128))

            display_data.set_pixel(3, 5, (0, 0, 128))
            display_data.set_pixel(4, 5, (0, 0, 128))
            display_data.set_pixel(5, 5, (0, 0, 128))

            display_data.set_pixel(4, 4, (0, 0, 128))
            display_data.set_pixel(4, 3, (0, 0, 128))
            display_data.set_pixel(4, 2, (0, 0, 128))

            display_data.set_pixel(3, 3, (0, 0, 128))
            display_data.set_pixel(5, 3, (0, 0, 128))
            display_data.set_pixel(2, 4, (0, 0, 128))
            display_data.set_pixel(6, 4, (0, 0, 128))

            display_data.set_pixel(3, 1, (0, 0, 128))
            display_data.set_pixel(2, 0, (0, 0, 128))
            display_data.set_pixel(6, 0, (0, 0, 128))
            display_data.set_pixel(5, 1, (0, 0, 128))

        if self.__in:

            display_data.set_pixel(3, 7, (0, 0, 128))
            display_data.set_pixel(4, 7, (0, 0, 128))
            display_data.set_pixel(5, 7, (0, 0, 128))

            display_data.set_pixel(3, 6, (0, 0, 128))
            display_data.set_pixel(5, 6, (0, 0, 128))

            display_data.set_pixel(3, 5, (0, 0, 128))
            display_data.set_pixel(4, 5, (0, 0, 128))
            display_data.set_pixel(5, 5, (0, 0, 128))

            display_data.set_pixel(4, 4, (0, 0, 128))
            display_data.set_pixel(4, 3, (0, 0, 128))
            display_data.set_pixel(4, 2, (0, 0, 128))

            display_data.set_pixel(3, 3, (0, 0, 128))
            display_data.set_pixel(5, 3, (0, 0, 128))
            display_data.set_pixel(2, 2, (0, 0, 128))
            display_data.set_pixel(6, 2, (0, 0, 128))

            display_data.set_pixel(3, 1, (0, 0, 128))
            display_data.set_pixel(3, 0, (0, 0, 128))
            display_data.set_pixel(5, 0, (0, 0, 128))
            display_data.set_pixel(5, 1, (0, 0, 128))
