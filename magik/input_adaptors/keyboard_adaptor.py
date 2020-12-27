import sys
import select
import tty
import termios
import time

from .base_input_adaptor import BaseInputAdaptor

def isData():
    counter = 0
    while counter < 30:
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return True
        counter += 1
        time.sleep(0.1)
    return False

KEY_MAP = {
    "q": (0, 0, 0),
    "Q": (0, 0, 1),
    "w": (1, 0, 0),
    "W": (1, 0, 1),
    "e": (2, 0, 0),
    "E": (2, 0, 1),
    "a": (0, 1, 0),
    "A": (0, 1, 1),
    "s": (1, 1, 0),
    "S": (1, 1, 1),
    "d": (2, 1, 0),
    "D": (2, 1, 1),
    "z": (0, 2, 0),
    "Z": (0, 2, 1),
    "x": (1, 2, 0),
    "X": (1, 2, 1),
    "c": (2, 2, 0),
    "C": (2, 2, 1),
}

class KeyboardAdaptor(BaseInputAdaptor):
    def __init__(self):
        super().__init__()
        tty.setcbreak(sys.stdin.fileno())

    def read(self, delta, input_data):
        key = sys.stdin.read(1)
        if isData():
            key_mapping = KEY_MAP.get_item(key)
            if not key_mapping is None:
                x_coord, y_coord, value = key_mapping

                if input_data.is_x_valid(x_coord) \
                        and input_data.is_y_valid(y_coord): 
                    input_data.set_input(x_coord, y_coord, value)

