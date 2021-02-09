try:
    from utime import ticks_ms as get_clock
except:
    import time
    def get_clock():
        return round(time.time() * 1000)

class Sprite:
    """ Base class for all sprite implementations """

    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        """ Initializes a sprite

        :param x: The starting x coordinate of the sprite
        :type x: Number
        :param y: The starting y coordinate of the sprite
        :type y: Number
        :param width: The width of the sprite
        :type width: Number
        :param height: The height of the sprite
        :type height: Number
        """

        self._x = x
        self._y = y
        self._width = width
        self._height = height

        self._destroyed = False
        self._game = None
        self._bounding_box = None

        self._update_bounding_box()
        self._prev_time = get_clock()

    def _update_bounding_box(self):
        """ Updates the bounding box for the sprite based on its position, width
        and height """
        bottom_right_x = self._x + self._width
        bottom_right_y = self._y + self._height
        self._bounding_box = ((self._x, self._y),
                                            (bottom_right_x, bottom_right_y))

    def has_timer_expired(self, duration, reset=True):
        """ Returns true if the requested duration has elapsed since the last
        time that the timer was cleared.

        :param duration: The duration in milliseconds
        :type duration: Number
        :param reset: If true, resets the timer after each read. Optional value,
                      defaults to True if omitted
        :param reset: Boolean
        """
        if get_clock() - self._prev_time > duration:
            if reset == True:
                self._prev_time = get_clock()
            return True
        return False


    def set_position(self, x, y):
        """ Updates position of the sprite and recalculates bounding box

        :param x: The x coordinate of the sprite
        :type x: Number
        :param y: The y coordinate of the sprite
        :type y: Number
        """

        self._x = x
        self._y = y
        self._update_bounding_box()

    def set_dimensions(self, x, y):
        """ Updates dimensions of the sprite and recalculates bounding box

        :param width: The width coordinate of the sprite
        :type width: Number
        :param height: The height coordinate of the sprite
        :type height: Number
        """

        self._width = width
        self._height = height
        self._update_bounding_box()

    def set_game(self, game):
        """ Sets game reference.

        :param game: Reference to the game object
        :type game: Game
        """

        self._game = game

    def destroy(self):
        """ Destroys current sprite, making the game remove it from the loop
        """

        self._destroyed = True

    def update(self, input_data):
        """ Updates sprite. This method should be overridden by child classes.
        Current implementation only updates bounding box.

        :param input_data: Object containing user inputs
        :type input_data: InputData
        """
        self._update_bounding_box()


    def draw(self, display_data):
        """ Draws the sprite on a display. Must be implemented by child class

        :param display_data: Object representing the display
        :type display_data: DisplayData
        """

        pass

    def is_colliding(self, box):
        """ Detects if current sprite collides with the box 

        :param box: A pair of tuples that represent the top right and bottom left
        of the box
        :type box: ((Number, Number), (Number, Number))
        """
        # TODO: Implement function
        return False
    
    @property
    def destroyed(self):
        """ Returns True if sprite is destroyed, and False otherwise
        """
        return self._destroyed
    
    @property
    def x(self):
        """ Returns the x coordinate of the sprite """
        return self._x

    @property
    def y(self):
        """ Returns the y coordinate of the sprite """
        return self._y
    
    @property
    def width(self):
        """ Returns the width of the sprite """
        return self._width

    @property
    def height(self):
        """ Returns the height of the sprite """
        return self._height

    @property
    def bounding_box(self):
        """ Returns the bounding box of the sprite """
        return self._bounding_box

    
