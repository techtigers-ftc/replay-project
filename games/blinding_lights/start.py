from magik.display_adaptors import AsciiAdaptor as DisplayAdaptor
# from magik.display_adaptors.np_adaptor import NeoPixelAdaptor as DisplayAdaptor
from magik.input_adaptors import KeyboardAdaptor as InputAdaptor
from magik import Controller
from magik import Game
from floor_is_lava import Lava


# Initialize game object and configure it
game = Game()
game.set_display_dimensions(8, 8)
game.set_input_dimensions(3, 3)

# Create a single space ship sprite and add it to the game
game.add_sprite(Lava(0))
game.add_sprite(Lava(1))
game.add_sprite(Lava(2))
game.add_sprite(Lava(3))
game.add_sprite(Lava(4))
game.add_sprite(Lava(5))
game.add_sprite(Lava(6))
game.add_sprite(Lava(7))

# Initialize the controller and adapters for input and output
display_adaptor = DisplayAdaptor()
input_adaptor = InputAdaptor()
controller = Controller()

# Configure the controller
controller.set_display_adaptor(display_adaptor)
controller.set_input_adaptor(input_adaptor)
controller.set_frame_rate(60)

# Ask the controller to run our game
controller.set_game(game)

# Start the controller
controller.start()
