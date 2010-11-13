"""
exceptions.py
"""

from .base import Response

class WsgiException(Exception):
    """
    WsgiException
    """
    
    def __init__(self, status):
        """
        Defaults to 500 Internal Server Error
        """
        self.response = Response(status = status)
