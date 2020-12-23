from magik.adaptors.ascii_adaptor import AsciiAdaptor
from magik import Inputs
from magik import InputAdaptor
# from magik.micro_adaptors.np_adaptor import NeoPixelAdaptor
from magik import Display
from magik import Controller
from games.game import Game

game = Game()
display = Display(3, 3)
adaptor = AsciiAdaptor(display)
inputs = Inputs(2, 2)
input_adaptor = InputAdaptor(inputs)
controller = Controller(game, display, adaptor, inputs, input_adaptor)
controller.start()
