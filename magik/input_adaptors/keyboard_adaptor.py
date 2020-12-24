from ..input_adaptor import InputAdaptor
class KeyboardAdaptor(InputAdaptor):
    def __init__(self):
        super().__init__()

    def read(self, delta, input_data):
        x = int(input("Type x value"))
        y = int(input("Type y value"))
        value = int(input("Type value"))
        input_data.set_input(x, y, value)
