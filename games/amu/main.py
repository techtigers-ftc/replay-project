from magik import Controller
from magik import Game
from magik.input_adaptors import DefaultAdaptor as InputAdaptor
from magik.display_adaptors import DefaultAdaptor as DisplayAdaptor

from games.amu.person import Person

def play():
    """ Launches the game """

    # Initialize game object and configure it
    game = Game()
    game.set_display_dimensions(8, 8)
    game.set_input_dimensions(3, 3)
    
    # Create a single space ship sprite and add it to the game
    person_sprite = Person(0, 0)
    game.add_sprite(person_sprite)
    
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

if __name__ == "__main__":
    # File is called as a script, not import - start the game
    play()