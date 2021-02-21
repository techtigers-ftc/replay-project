""" Module for BaseInputAdaptor class """

class BaseInputAdaptor: # pylint:disable=too-few-public-methods
    """ Abstract input adaptor class, do not use directly, always create child
        class
    """
    def __init__(self):
        pass
    
    def setup(self, input_data):
        """Provides a setup option for the child classes to prepare before the
        game starts
        
        :param input_data: refrence to input data object 
        :type input_data: InputData
        """
        pass 

    def read(self, input_data): # pylint:disable=no-self-use
        """ Read input from physical device
        
        :param input_data: refrence to input data object 
        :type input_data: InputData
        """
        raise Exception("Not implemented")
