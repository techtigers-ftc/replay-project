from magik.adaptors.np_adaptor import NeoPixelAdaptor
from magik import InputData
from magik.input_adaptors import KeyboardAdaptor
from magik import DisplayData
from magik import Controller
from test_game import TestGame

game = TestGame()
display_adaptor = NeoPixelAdaptor()
input_adaptor = KeyboardAdaptor()
controller = Controller()

controller.set_display_adaptor(display_adaptor)
controller.set_game(game)
controller.set_input_adaptor(input_adaptor)
controller.set_frame_rate(60)

controller.start()
