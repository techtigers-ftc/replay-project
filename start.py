# from magik.display_adaptors.np_adaptor import NeoPixelAdaptor as DisplayAdaptor
from magik.display_adaptors.np_adaptor import NeoPixelAdaptor as DisplayAdaptor
from magik import InputData
from magik.input_adaptors import GPIOAdaptor as InputAdaptor
from magik import DisplayData
from magik import Controller
from test_game import TestGame

game = TestGame()
display_adaptor = DisplayAdaptor()
input_adaptor = InputAdaptor()
controller = Controller()

controller.set_display_adaptor(display_adaptor)
controller.set_game(game)
controller.set_input_adaptor(input_adaptor)
controller.set_frame_rate(60)

controller.start()
