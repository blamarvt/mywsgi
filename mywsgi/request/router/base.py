"""
base.py
"""

__config_section__ = "mywsgi.request.router"

class Router(object):
    """
    Router
    """
        
    def __init__(self, config):
        """
        Given a config object, make me a router!
        """
        self.config = config

    def route(self, request):
        """
        Given a WSGI Request object, route the request
        to the correct handler.
        """
        pass
