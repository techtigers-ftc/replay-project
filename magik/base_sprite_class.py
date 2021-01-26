# TODO: [REVIEW] Do not include the word "class" in the name of the class.
# Update the file name also.

# TODO: [REVIEW] Include/update documentation

class BaseSpriteClass:

    def __init__(self):
        # TODO: [REVIEW] Might be a good idea to make the bounding box a protected
        # variable, and expose each of the variables below as read-only properties
        self.bounding_box = 0
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0

    def update(self, input_data):
        # TODO: [REVIEW] A better naming convention to use would be top-left and
        # bottom-right. So you can use bottom_right_x instead of right_corner_x.
        # If you think about it, right_corner_x could mean left corner or right,
        # and this makes it a little ambiguous
        right_corner_x = self._x + self._width
        right_corner_y = self._y + self._height
        self.bounding_box = ((self._x, self._y),(right_corner_x, right_corner_y))

    def draw(self, display_data):
        pass

    # TODO: [REVIEW] Implement a method that checks if this sprite is colliding with
    # another bounding box. You can use that in a collision detection routine within
    # the game class.
    
    # TODO: [REVIEW] Consider implementing a set_position() function to move the
    # sprite to a specific location
    
    # TODO: [REVIEW] Consider implementing a function that will allow a sprite to
    # destroy itself (you are already handing the removal of the sprite in the game
    # class
    
    # TODO: [REVIEW] Consider implementing a set_dimensions() function that can be used
    # to set the width and height of the sprite
    
    
    
