from magik.adaptors.ascii_adaptor import AsciiAdaptor
from magik import Inputs
from magik import InputAdaptor
# from magik.micro_adaptors.np_adaptor import NeoPixelAdaptor
from magik import Display
from magik import Controller
from games.game import Game

game = Game()
inputs = Inputs(2,2)
controller = Controller()
controller.set_display(Display(3,3), AsciiAdaptor)
controller.set_game(game)
controller.set_input(inputs)
input_adaptor = InputAdaptor(inputs)
controller.start()
