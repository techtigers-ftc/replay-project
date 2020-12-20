class InputAdaptor:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.inputs = []

        for x in range(self.height):
            self.inputs.append([])
            for y in range(self.width):
                self.inputs[x].append(0)

    def set_input(self, x, y,value):
        self.inputs[x][y] = value

    def read_raw_input():
        pass

    def get_inputs(self):
        return inputs

    def test(self): 
        self.set_input(1,1,5)


