"""
xml.py
"""

import httplib
import lxml.etree

from .base import Response

class XmlResponse(Response):
    """
    An XML formatted response.
    """

    def __init__(self, status, content = None, headers = None):
        """
        Create an XML response.
        """
        Response.__init__(self, status, content, headers)
        self.content_type = "application/xml"
        self.content = lxml.etree.tostring(self.content)
