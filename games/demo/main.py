from magik import launch_single_tile

from games.demo.tile import Tile

def play():
    """ Launches the game """

    sprites = [
        Tile(0, 0)
    ]
    
    launch_single_tile(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()

