from magik import launch_single_tile
from magik.display_adaptors import AsciiAdaptor as DisplayAdaptor
from magik.display_adaptors.np_adaptor import NeoPixelAdaptor as DisplayAdaptor
from magik.input_adaptors import KeyboardAdaptor as InputAdaptor
from magik import Controller
from magik import Game
from chair import Chair

def play():
    """ Launches the game """

    sprites = [
        Chair(7, 7)
    ]
    
    launch_single_tile(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
