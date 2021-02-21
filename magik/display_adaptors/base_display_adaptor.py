""" Module for DisplayAdaptor class """

class BaseDisplayAdaptor: # pylint:disable=too-few-public-methods
    """ Abstract display adaptor class, do not use directly, always create child
        class
    """
    def __init__(self):
        pass
    
    def setup(self, display_data):
        """Provides a setup option for the child classes to prepare before the game starts

        :param display_data: refrence to display data object 
        :type display_data: DisplayData
        """
        pass 

    def show(self,  display_data): # pylint:disable=no-self-use
        """Show output on a physical device

        :param display_data: refrence to display data object 
        :type display_data: DisplayData
        """
        raise Exception("Not implemented")
