# import turtle

def get_color(rgb):
    (r, g, b) = rgb
    if r == 1:
        return "red"
    elif g == 1:
        return "green"
    elif b == 1:
        return "blue"
    else:
        return "black"

class TurtleAdaptor:
    def __init__(self, display):
        # turtle.tracer(False)
        # self.display = display
        pass

    def show(self, delta):
        pass
        # x_offset = -self.display.width / 2;
        # y_offset = -self.display.height / 2;
        # size = 20

        # turtle.penup()
        # turtle.setpos(self.display.width/-2, self.display.height/2)
        # turtle.pendown()
        # turtle.pu()

        # x = 0
        # y = 0
        # for row in self.display.get_pixels():
        #     turtle.setpos(x_offset, y_offset + (y * size))
        #     # turtle.setpos(self.display.width/-2, abs(self.display.height)/2 - (pixels.index(row)*10))
        #     for pixel in row:
        #         color = get_color(pixel)
        #         turtle.dot(size,"{}".format(color))
        #         turtle.fd(size)
        #     y = y - 1
