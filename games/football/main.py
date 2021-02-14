from magik import Controller
from magik import Game
from magik.input_adaptors import DefaultAdaptor as InputAdaptor
from magik.display_adaptors import DefaultAdaptor as DisplayAdaptor

from games.football.hb import Halfback
from games.football.qb import Quarterback
from games.football.ol import OLine
from games.football.dl import DLine

""" Launches the game """

# Initialize game object and configure it
game = Game()
game.set_display_dimensions(8, 8)
game.set_input_dimensions(2, 2)

# Create a single space ship sprite and add it to the game
# space_ship_sprite = Box(0, 0, 1, 0)
# game.add_sprite(space_ship_sprite)
hb = Halfback(3, 1)
qb = Quarterback(4, 1)
ol_1 = OLine(3, 3)
ol_2 = OLine(4, 3)
ol_3 = OLine(5, 3)
dl_1 = DLine(3, 4)
dl_2 = DLine(4, 4)
dl_3 = DLine(5, 4)

game.add_sprite(hb)
game.add_sprite(qb)
game.add_sprite(ol_1)
game.add_sprite(ol_2)
game.add_sprite(ol_3)
game.add_sprite(dl_1)
game.add_sprite(dl_2)
game.add_sprite(dl_3)

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
