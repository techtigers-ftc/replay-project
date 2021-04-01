from magik import launch_single_tile

from games.quadrant.quadrant import Quadrant

def play():
    """ Launches the game """

    sprites = [
        Quadrant(0, 0)
    ]
    
    launch_single_tile(sprites, input_adaptor_type='raw')

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
