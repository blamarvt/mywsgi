"""
plaintext.py
"""

import httplib

from .base import Response

class PlainTextResponse(Response):
    """
    Base class for all responses in the `mywsgi` framework.
    """

    def __init__(self, content):
        """
        Create a plain-text response.
        """
        Response.__init__(self, status = 200, content = content)
        self.content_type = "text/plain"
