from magik import Controller
from magik import Game
from magik.input_adaptors import DefaultAdaptor as InputAdaptor
from magik.display_adaptors import DefaultAdaptor as DisplayAdaptor
from magik import Sprite
import time

from games.avaneesh_game.ball import Ball
from games.avaneesh_game.ball2 import Ball2
from games.avaneesh_game.ball3 import Ball3
from games.avaneesh_game.winner import Winner

# Initialize game object and configure it
game = Game()
game.set_display_dimensions(9, 9)
game.set_input_dimensions(3, 3)
# Create a single ball sprite and add it to the game
ball_sprite_1 = Ball(1, 1)
ball_sprite_2 = Ball2(4,1)
ball_sprite_3 = Ball3(3,2)
winner_sprite = Winner(1,4)

game.add_sprite(ball_sprite_2)
game.add_sprite(ball_sprite_1)
game.add_sprite(ball_sprite_3)
game.add_sprite(winner_sprite)
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

