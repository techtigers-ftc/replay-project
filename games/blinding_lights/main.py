from magik import launch_single_tile

from floor_is_lava import Lava

def play():
    sprites = [
        Lava(0),
        Lava(1),
        Lava(2),
        Lava(3),
        Lava(4),
        Lava(5),
        Lava(6),
        Lava(7)
    ]

    launch_single_tile(sprites)

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()
