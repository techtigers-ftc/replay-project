from magik import launch_module

from games.football.hb import Halfback
from games.football.qb import Quarterback
from games.football.ol import OLine
from games.football.dl import DLine
from games.football.lb import Linebacker

def play():
    """ Launches the game """
    sprites = [
        Halfback(3, 1),
        Quarterback(4, 1),
        OLine(3, 3),
        OLine(4, 3),
        OLine(5, 3),
        DLine(3, 4),
        DLine(4, 4),
        DLine(5, 4),
        Linebacker(4, 5)
    ]

    launch_module(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
