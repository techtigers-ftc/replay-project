from magik import launch_single_tile

from games.intro.box import Box

def play():
    """ Launches the game """

    sprites = [
        Box(3, 3, 0, 0)
    ]
    
    launch_single_tile(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
