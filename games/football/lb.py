from games.football.player import Player

class Linebacker(Player):
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
        self._colors = [(32, 0, 0), (0, 32, 0), (0, 0, 32), (32, 32, 0), \
                (32, 0, 32), (0, 32, 32), (32, 32, 32)]
        self._color = self._colors[0]
        self._counter = 0
        self._movement = [(1, 0, 0), (1, 0, 0), (1, -1, 0)]
        self._carrier = False

    def update(self, input_data):
        if self.has_timer_expired(500):
            if not self._counter >= len(self._movement):
                move = self._movement[self._counter]
                self.move(move[0], move[1])
                if move[2] == 1:
                    self._carrier = True
                else:
                    self._carrier = False

            self._counter += 1

        if self._carrier:
            self._color = self._colors[6]
        else:
            self._color = self._colors[0]


    def draw(self, display_data):
        display_data.set_pixel(self.x, self.y, self._color)

