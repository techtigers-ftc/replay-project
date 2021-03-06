from games.football.player import Player

class Halfback(Player):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self._colors = [(32, 0, 0), (0, 32, 0), (0, 0, 32), (32, 32, 0), \
                (32, 0, 32), (0, 32, 32), (32, 32, 32)]
        self._color = self._colors[0]
        self._trail_color = self._colors[3]
        self._counter = 0
        self._movement = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1),\
                (0, 1, 1), (0, 1, 1), (0, 1, 1)]
        self._prev_movements = []
        self._carrier = False

    def update(self, input_data):
        # if self.has_timer_expired(500):
            # if len(self._prev_movements) >= 5:
            #     self._prev_movements.pop(0)
            # self._prev_movements.append((self.x, self.y))

            # if not self._counter >= len(self._movement):
            #     move = self._movement[self._counter]
            #     self.move(move[0], move[1])
                # if move[2] == 1:
                #     self._carrier = True
                # else:
                #     self._carrier = False

            # self._counter += 1

        # if self._carrier:
        #     self._color = self._colors[6]
        # else:
        #     self._color = self._colors[0]

        if input_data.get_input(0,0) == 1:
            self._color = self._colors[1]
        # elif input_data.get_input(1,0) == 1:
        #     self._color = self._colors[2]
        # elif input_data.get_input(0,1) == 1:
        #     self._color = self._colors[3]
        # elif input_data.get_input(1,1) == 1:
        #     self._color = self._colors[4]
        else:
            self._color = self._colors[0]

    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, self._color)

        # for movement in self._prev_movements:
        #     display_data.set_pixel(movement[0], movement[1], self._trail_color)
