class Inputs:
    # Init with initial variables
    def __init__(self, x_length, y_length):
        self.x_length = x_length
        self.y_length = y_length
        self.inputs = []
        self.reference = []
        
        for x in range(self.y_length):
            self.inputs.append([])
            self.reference.append([])
            for y in range(self.x_length):
                self.inputs[x].append(0)
                self.reference[x].append(0)

    def clear(self):
        for x in range(0, self.y_length):
            for y in range(self.x_length):
                self.reference[x][y] = 0

    def set_reference(self):
        for y in range(len(self.inputs)):
            for x in range(len(self.inputs)):
                self.reference[y][x] = self.inputs[y][x]
        self.reference = self.inputs

    def input_value(self, x, y):
        print(self.inputs, self.reference, x, y)
        return self.inputs[x][y] - self.reference[x][y]
