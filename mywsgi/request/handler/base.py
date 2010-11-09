"""
base.py
"""

__config_section__ = "mywsgi.request.handler"

class Handler(object):
    """
    Handler
    """

    def __init__(self, config):
        """
        Given a config object, make a handler!
        """
        self.config = config

    def handle(self, request):
        """
        Handle the given request.
        """
        pass
