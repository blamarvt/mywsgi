"""
config.py
"""

class Config(object):
    """
    Config
    """

    def __init__(self):
        """
        Create a configuration object which will be used
        by basically everything in `mywsgi`.
        """
        pass

class DefaultConfig(object):
    """
    DefaultConfig
    """
    
    def __init__(self):
        """
        Used to notify the user that they are using defaults
        from the code!
        """
        logging.warn("No configuration file specified, using 'safe' defaults.")

    def __call__(self, _, _, default, transform=str):
        """
        Always return None to ensure all defaults are used. If default
        is not supplied in the code, this will cause a crash!
        """
        return default
