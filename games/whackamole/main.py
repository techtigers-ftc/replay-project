from magik import launch_single_tile

from games.whackamole.mole import Mole

def play():
    """Launches the game"""

    sprites = [
        Mole()
    ]

    launch_single_tile(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
