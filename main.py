from magik.adaptors.ascii_adaptor import AsciiAdaptor
from magik import Display
from magik import Controller
from games.game import Game

game = Game()
display = Display(3, 3)
adaptor = AsciiAdaptor(display)
controller = Controller(game, display, adaptor)
controller.start()
