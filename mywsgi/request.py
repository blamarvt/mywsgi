"""
Model an HTTP request as an object. 
"""

from mywsgi.exceptions import UriTooLong

class Request(object):
    """
    An HTTP request object class.
    """

    def __init__(self, environ):
        """
        Parse the environment into class variables.
        Save a copy of the environ in case in needs to be used in
        it's natural form.
        """
        self.environ = environ
        environ = environ.copy()

        self.path = environ["PATH_INFO"]
        self.method = environ["REQUEST_METHOD"]
        self.content_type = environ["CONTENT_TYPE"]
        self.input = environ["wsgi.input"]

        try:
            self.get = dict([part.split('=') for part in environ["QUERY_STRING"].split('&')])
        finally:
            self.get = {}

