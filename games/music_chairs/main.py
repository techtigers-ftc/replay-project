from magik import launch_single_tile
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
