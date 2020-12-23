class KeyboardInput:
    def __init__(self, inputs):
        self.inputs = inputs


    def set_input(self, x, y,value):
        self.inputs.inputs[x][y] = value
        print(self.inputs.inputs)

    def read_raw_input(self):
        x = int(input("Type x value"))
        y = int(input("Type y value"))
        value = int(input("Type value"))
        self.set_input(x, y, value)

    def test(self): 
        self.set_input(1,1,5)


