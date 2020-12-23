""" Module for DisplayAdaptor class """

class DisplayAdaptor: # pylint:disable=too-few-public-methods
    """ Abstract display adaptor class, do not use directly, always create child
        class
    """
    def __init__(self):
        pass

    def show(self,  output_data): # pylint:disable=no-self-use
        """ Show output on a physical device
        """
        raise Exception("Not implemented")
