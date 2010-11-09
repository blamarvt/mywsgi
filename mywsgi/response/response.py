"""
response.py
"""

class Response(object):
    """
    TODO: Define the mywsgi.response.Response class here
    """
    
    def __init__(self, config, view):
        """
        Given a configuration object and a mywsgi.View,
        create a Response class instance.
        """
        self.config = config
        self.view = view
