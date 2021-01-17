class BaseSpriteClass:

    def __init__(self):
        """ Base class for a sprite
        """
        pass

    def update(self,x,y):
        """ to move the position of the sprite
            :param x: used to set x of sprite
            :type x: var
            :param y: used to set y of sprite
            :type y: var
        """
        raise Exception("Not implemented")


    def write(self, display):
        """ to write it onto the display
            
            :param display: display class for child class to use to write pixels
            :type display: instance of display class
        """
        raise Exception("Not implemented")
