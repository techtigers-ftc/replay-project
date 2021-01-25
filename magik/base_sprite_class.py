class BaseSpriteClass:

    def __init__(self):
        self.bounding_box = 0
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0

    def update(self, input_data):
        right_corner_x = self._x + self._width
        right_corner_y = self._y + self._height
        self.bounding_box = ((self._x, self._y),(right_corner_x, right_corner_y))

    def draw(self, display_data):
        pass
