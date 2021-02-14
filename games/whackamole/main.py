from magik import Controller
from magik import Game
from magik.input_adaptors import DefaultAdaptor as InputAdaptor
from magik.display_adaptors import DefaultAdaptor as DisplayAdaptor

from games.whackamole.mole import Mole

""" Launches the game """

# Initialize game object and configure it
game = Game()
game.set_display_dimensions(8, 8)
game.set_input_dimensions(2, 2)

# Create a single space ship sprite and add it to the game
# space_ship_sprite = Box(0, 0, 1, 0)
# game.add_sprite(space_ship_sprite)
mole = Mole()

game.add_sprite(mole)

# Initialize the controller and adapters for input and output
display_adaptor = DisplayAdaptor()
input_adaptor = InputAdaptor()
controller = Controller()

# Configure the controller
controller.set_display_adaptor(display_adaptor)
controller.set_input_adaptor(input_adaptor)
controller.set_frame_rate(20)

# Ask the controller to run our game
controller.set_game(game)

# Start the controller
controller.start()
