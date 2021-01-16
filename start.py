from magik.display_adaptors.ascii_adaptor import AsciiAdaptor as DisplayAdaptor
# from magik.display_adaptors.np_adaptor import NeoPixelAdaptor as DisplayAdaptor
from magik import InputData
from magik.input_adaptors import KeyboardAdaptor as InputAdaptor
from magik import DisplayData
from magik import Controller
from magik import Game
from first_sprite import FirstSprite

sprites = []
counter = 0
while counter < 10:
    sprites.append(FirstSprite())
    counter += 1
game = Game(sprites)
game.set_display_dimensions(8, 8)
display_adaptor = DisplayAdaptor()
input_adaptor = InputAdaptor()
controller = Controller()

controller.set_display_adaptor(display_adaptor)
controller.set_game(game)
controller.set_input_adaptor(input_adaptor)
controller.set_frame_rate(60)

controller.start()
