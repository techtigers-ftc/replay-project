from magik import launch_module

from games.big_intro.box import Box

def play():
    """ Launches the game """

    sprites = [
        Box(7, 15, 0, 0)
    ]
    
    launch_module(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
