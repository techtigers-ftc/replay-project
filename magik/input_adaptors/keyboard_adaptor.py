from .base_input_adaptor import BaseInputAdaptor
import sys
import select
import tty
import termios
import time
from .key import Key

def isData():
    counter = 0
    while counter < 30:
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return True
        counter += 1
        time.sleep(0.1)
    return False

class KeyboardAdaptor(BaseInputAdaptor):
    def __init__(self):
        super().__init__()

    def read(self, delta, input_data):
        key = Key()
        key_arr = [key.create_dict('q', 0, 0), key.create_dict('w', 0, 1), 
                key.create_dict('e', 0, 2), key.create_dict('a', 1, 0), 
                key.create_dict('s', 1, 1), key.create_dict('d', 1, 2),
                key.create_dict('z', 2, 0), key.create_dict('x', 2, 1),
                key.create_dict('c', 2, 2), key.create_dict('', 0, 0)]
        print(key_arr)
        tty.setcbreak(sys.stdin.fileno())
        value = sys.stdin.read(1)
        if isData():
            print(value)
            if key.check_key_press('q', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('w', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('e', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('a', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('s', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('d', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('z', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('x', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)
            if key.check_key_press('c', value, key_arr):
                key.set_key_value('q', 1, input_data, key_arr)

