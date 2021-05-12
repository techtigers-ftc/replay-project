from magik import Controller
from magik import Game
from magik.input_adaptors import RawAdaptor, DefaultAdaptor, RawAdaptor2
from magik.display_adaptors import DefaultAdaptor as DisplayAdaptor

def launch_single_tile(sprites, **input_adaptor_type):
    """ Launches a game on a single tile (8x8) mat that has (2x2) pressure
    sensors. The game is configured with default values, and initialized using
    the provided sprites. Can switch between debouncing and sending raw inputs.

    :param sprites: A collection of sprites to add to the game.
    :type sprites: Any array of sprites to add to the game.
    :param input_adapor_type: Can switch between debouncing and raw input
    :type input_adaptor_type: kwarg 


    """

    # Initialize game object and configure it
    game = Game()
    game.set_display_dimensions(8, 8)
    game.set_input_dimensions(2, 2)

    # Create a single space ship sprite and add it to the game
    for sprite in sprites:
        game.add_sprite(sprite)

    # Initialize the controller and adapters for input and output
    display_adaptor = DisplayAdaptor()
    if 'input_adaptor_type' in input_adaptor_type and input_adaptor_type['input_adaptor_type'] == 'raw':
        input_adaptor = RawAdaptor()
    else:
        input_adaptor = DefaultAdaptor()

    controller = Controller()

    # Configure the controller
    controller.set_display_adaptor(display_adaptor)
    controller.set_input_adaptor(input_adaptor)
    controller.set_frame_rate(20)

    # Ask the controller to run our game
    controller.set_game(game)

    # Start the controller
    controller.start()



def launch_module(sprites, **input_adaptor_type):
    """ Launches a game on a module (32x16) mat that has (4x2) pressure
    sensors. The game is configured with default values, and initialized using
    the provided sprites. Can switch between debouncing and sending raw inputs.

    :param sprites: A collection of sprites to add to the game.
    :type sprites: Any array of sprites to add to the game.
    :param input_adapor_type: Can switch between debouncing and raw input
    :type input_adaptor_type: kwarg 


    """

    # Initialize game object and configure it
    game = Game()
    game.set_display_dimensions(16, 32)
    game.set_input_dimensions(2, 3)

    # Create a single space ship sprite and add it to the game
    for sprite in sprites:
        game.add_sprite(sprite)

    # Initialize the controller and adapters for input and output
    display_adaptor = DisplayAdaptor()
    input_adaptor = RawAdaptor2()

    controller = Controller()

    # Configure the controller
    controller.set_display_adaptor(display_adaptor)
    controller.set_input_adaptor(input_adaptor)
    controller.set_frame_rate(20)

    # Ask the controller to run our game
    controller.set_game(game)

    # Start the controller
    controller.start()
