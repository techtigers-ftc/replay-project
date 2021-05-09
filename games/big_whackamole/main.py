from magik import launch_module

from games.big_whackamole.mole import Mole
from games.big_whackamole.score import Score

def play():
    """Launches the game"""

    sprites = [
        Mole(Score())
    ]

    launch_module(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
