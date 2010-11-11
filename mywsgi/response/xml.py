"""
xml.py
"""

import httplib
import lxml.etree

class XmlResponse(object):
    """
    Base class for all responses in the `mywsgi` framework.
    """

    status_code = httplib.OK

    def get_content(self):
        """
        Retrieve the content of this response in JSON format.
        """
        return lxml.etree.tostring(root)
