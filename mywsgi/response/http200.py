"""
http200.py
"""

import httplib

class NoContentResponse(Response):
    """
    204 No Content
    """
    
    def __init__(self):
        """
        Return a "no content" response.
        """
        Response.__init__(self, 204, content = "", headers = "")
