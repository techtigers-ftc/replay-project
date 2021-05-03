from magik import launch_single_tile

from games.avaneesh_game.ball import Ball
from games.avaneesh_game.ball2 import Ball2
from games.avaneesh_game.ball3 import Ball3
from games.avaneesh_game.winner import Winner

def play():
    sprites = [
        Ball(1,1),
        Ball2(4,1),
        Ball3(3,2)
        ]

    launch_single_tile(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
