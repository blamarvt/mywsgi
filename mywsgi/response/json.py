"""
json.py
"""

import httplib
import simplejson as json

from .base import Response

class JsonResponse(Response):
    """
    A JSON formatted response.
    """

    def __init__(self, status, content = None, headers = None):
        """
        Create a JsonResponse.
        """
        Response.__init__(self, status, content, headers)
        self.content_type = "application/json"
        self.content = json.dumps(self.content)
