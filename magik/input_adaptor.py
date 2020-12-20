
class InputAdaptor:
    def __init__(self, width, height, inputs):
        self.inputs = inputs


    def set_input(self, x, y,value):
        self.inputs[x][y] = value

    def read_raw_input():
        pass

    def test(self): 
        self.set_input(1,1,5)


