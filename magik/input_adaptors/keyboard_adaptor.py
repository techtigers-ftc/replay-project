from ..input_adaptor import InputAdaptor
import sys
import select
import tty
import termios
import time

def isData():
    counter = 0
    while counter < 10:
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return True
        counter += 1
        time.sleep(0.1)
    return False

class KeyboardAdaptor(InputAdaptor):
    def __init__(self):
        super().__init__()

    def read(self, delta, input_data):
        tty.setcbreak(sys.stdin.fileno())
        if isData():
            value = sys.stdin.read(1)

            print(value)
            if value == 'q':
                input_data.set_input(0, 0, 1)
            if value == 'w':
                input_data.set_input(0, 1, 1)
            if value == 'e':
                input_data.set_input(0, 2, 1)
            if value == 'a':
                input_data.set_input(1, 0, 1)
            if value == 's':
                input_data.set_input(1, 1, 1)
            if value == 'd':
                input_data.set_input(1, 2, 1)
            if value == 'z':
                input_data.set_input(2, 0, 1)
            if value == 'x':
                input_data.set_input(2, 1, 1)
            if value == 'c':
                input_data.set_input(2, 2, 1)
