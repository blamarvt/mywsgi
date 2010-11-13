"""
config.py
"""

import logging

class Configuration(object):
    """
    Configuration
    """

    def __init__(self):
        """
        Create a configuration object which will be used
        by basically everything in `mywsgi`.
        """
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')
        self.logger = logging.getLogger("mywsgi")
        
    def __call__(self, cls_instance, section, default, transform):
        """
        Retrieve configuration.
        """
        return default

    
