from magik.display_adaptors import AsciiAdaptor as DisplayAdaptor
# from magik.display_adaptors.np_adaptor import NeoPixelAdaptor as DisplayAdaptor
from magik.input_adaptors import KeyboardAdaptor as InputAdaptor
from magik import Controller
from magik import Game
from first_sprite import FirstSprite

game = Game()
first_sprite = FirstSprite()
game.add_sprite(first_sprite)

game.set_display_dimensions(9, 9)
game.set_input_dimensions(3, 3)
display_adaptor = DisplayAdaptor()
input_adaptor = InputAdaptor()
controller = Controller()

controller.set_display_adaptor(display_adaptor)
controller.set_game(game)
controller.set_input_adaptor(input_adaptor)
controller.set_frame_rate(60)

controller.start()
