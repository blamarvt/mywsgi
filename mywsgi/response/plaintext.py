"""
plaintext.py
"""

import httplib

from .base import Response

class PlainTextResponse(Response):
    """
    Base class for all responses in the `mywsgi` framework.
    """

    def __init__(self, status, content = None, headers = None):
        """
        Create a plain-text response.
        """
        Response.__init__(self, status, content, headers)
        self.content_type = "text/plain"
