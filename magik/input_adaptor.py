""" Module for InputAdaptor class """

class InputAdaptor: # pylint:disable=too-few-public-methods
    """ Abstract input adaptor class, do not use directly, always create child
        class
    """
    def __init__(self):
        pass

    def read(self, input_data): # pylint:disable=no-self-use
        """ Read input from physical device
        """
        raise Exception("Not implemented")
