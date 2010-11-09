"""
base.py
"""

import httplib

from mywsgi.util.exceptions import AbstractClassException

__config_section__ = "mywsgi.response"

class Response(object):
    """
    Base class for all responses in the `mywsgi` framework.
    """

    status_code = None

    def __init__(self, config, start_response):
        """
        @param config: A mywsgi.util.config object
        @param start_response: The standard WSGI start_response function
        """
        self.config = config
        self.start_response = start_response

        if self.__class__ is Response:
            raise AbstractClassException(cls = self.__class__)

    def __call__(self, content, headers):
        """
        @param content: A string, iterator, or file-like object
        @param headers: A list of tuples (header_name, value)
        """
        self.start_response(self.get_status(), headers or [])
        return content or ""

    def get_status(self):
        """
        Retrieve the HTTP status message for this response.
        (e.g. 200 OK, 403 Forbidden, 500 Internal Server Error)
        """
        return "%d %s" % (self.status_code, httplib.responses[self.status_code])
