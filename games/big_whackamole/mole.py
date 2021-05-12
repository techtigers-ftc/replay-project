from magik import Sprite
import random
from games.big_whackamole.success import Success
from games.big_whackamole.fail import Fail

class Mole(Sprite):
    """ Whackamole sprite class that allows the mole to move around and get whacked
    """
    def __init__(self, score):
        """ Innitializes the variables and params
        """
        x = random.randint(0, 13)
        y = random.randint(0, 21)
        super().__init__(x, y)

        self._display_states = [
            # [ (1, 0), (0, 1), (2, 1), (1, 2) ],
            # [ (0, 0), (0, 2), (2, 0), (2, 2) ]
            # [ (0,0), (1, 0), (2, 0) ],
            # [ (0,0), (1, 0), (2, 0), (0,1), (1, 1), (2, 1) ],
            [ (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (1, 2), (2, 2) ],
            [ (0, 0), (1, 0), (2, 0), (2, 1), (0, 2), (1, 2), (2, 2) ],
        ]
        self._colors = [
            (128, 0, 255)
        ]
        self._display_state_index = 0
        self._color_index = 0
        self._ticks = 0
        self._state = None
        self._x_input_areas = [ (0, 6), (7, 13) ]
        self._y_input_areas = [ (0, 6), (7, 13), (14, 21) ]
        self.__score = score

    def update(self, input_data):
        """ Is called every cycle and updates the position or state of the mole in game.

        :param input_data: instance of input data class
        :type input_data: InputData
        """
        if not self.has_timer_expired(100):
            return

        self._ticks += 1
        input_area = 0
        for x_coord in range(input_data.width):
            for y_coord in range(input_data.height):
                if self.x > x_coord * 8 and self.x < (x_coord + 1) * 8:
                    if self.y > y_coord * 8 and self.y < (y_coord + 1) * 8:
                        input_area = input_data.get_input(x_coord, y_coord)

                        
        # input_data.dump_input()
        print('----')
        # print(input_data.get_input(0,0))
        # print(input_data.get_input(0,1))
        # print(input_data.get_input(0,2))
        # print(input_data.get_input(1,0))
        # print(input_data.get_input(1,1))
        # print(input_data.get_input(1,2))

        # a = input_data.get_input(0,0)
        # b = input_data.get_input(0,1)
        # c = input_data.get_input(0,2)
        # d = input_data.get_input(1,0)
        # e = input_data.get_input(1,1)
        # f = input_data.get_input(1,2)


        if self._state is not None:
            if self._ticks > 5:
                self._game.add_sprite(Mole(self.__score))
                self.destroy()
        elif self._ticks >= 20:
            self._state= "FAIL"
            self._ticks = 0
            
        elif input_area > 100:
            self._state = "SUCCESS"
            self._ticks = 0
            self.__score.add(1)
        else:
            self._color_index = (self._color_index + 1) % len(self._colors)
            self._display_state_index = (self._display_state_index + 1) % \
                                                    len(self._display_states)


    def draw(self, display_data):
        """ Draws the updated sprite on the screen

        :param display_data: Instance of the display data class
        :type display_data: DisplayData
        """

        deltas = self._display_states[self._display_state_index]
        color = self._colors[self._color_index]

        if self._state == "SUCCESS":
            print("bruh")
            color = (0,255,0)
        elif self._state == "FAIL":
            color = (255,0,0)
        for index in range(len(deltas)):
            dx, dy = deltas[index]
            display_data.set_pixel(self.x + dx, self.y + dy, color)
