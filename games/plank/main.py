from magik import launch_module

from games.plank.sensor import Sensor
from games.plank.plank_state import PlankState

def play():
    """ Launches the game """

    plank_state = PlankState()
    sprites = [
        Sensor(0, 0, plank_state, "left"), 
        Sensor(0, 16, plank_state, "right"), 
    ]
    
    launch_module(sprites, input_adaptor_type='raw')

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
