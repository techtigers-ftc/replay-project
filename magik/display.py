class Display:
    # Init with initial variables
    def __init__(self, width, height):
        """ Is a abstract representation that can be used to develop games that many 
        different displays can use if paired with the right adapter
    
        :param width: how many pixels in one row
        :type width:int
        :param height: how mnay pixels in one column
        :type height:int
        """
        self.pixels = []
        self.height = height
        self.width = width
        # Sets the pixels array to all off
        for x in range(self.height):
            self.pixels.append([])
            for y in range(self.width):
                self.pixels[x].append((0,0,0))

    def clear_screen(self):
        """Clears the screen and sets all pixels to 0
        """
        for x in range(self.height):
            for y in range(self.width):
                self.pixels[x][y] = (0,0,0)

    def set_pixel(self, x,y,color):
        """Sets a certain pixel to a color
        """
        self.pixels[x][y] = color

    def get_pixels(self):
        """Returns the array with all pixels"""
        return self.pixels
