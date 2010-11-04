"""
request.py
"""

from collections import defaultdict
from urlparse import parse_qs

from mywsgi.util import Filelike, ContentType

class Request(object):
    """
    TODO: Define the mywsgi.request.Request class here
    """

    def __init__(self, config, environ):
        """
        Given a configuration object and a WSGI compliant environ,
        create a Request class instance.
        """
        self.config = config
        self.environ = environ.copy()

        # Parse WSGI specific items from environ
        self.wsgi_version = self.environ_parse('wsgi.version', tuple)
        self.wsgi_scheme = self.environ_parse('wsgi.url_scheme', str)
        self.wsgi_input = self.environ_parse('wsgi.input', self.create_filelike)
        self.wsgi_errors = self.environ_parse('wsgi.errors', self.create_filelike)
        self.wsgi_multithread = self.environ_parse('wsgi.multithread', bool)
        self.wsgi_multiprocess = self.environ_parse('wsgi.multiprocess', bool)
        self.wsgi_runonce = self.environ_parse('wsgi.run_once', bool)

        self.method = self.environ_parse('REQUEST_METHOD', str)
        self.script_name = self.environ_parse('SCRIPT_NAME', str)
        self.path_info = self.environ_parse('PATH_INFO', str)
        self.query_string = self.environ_parse('QUERY_STRING', str)
        self.content_type = self.environ_parse('CONTENT_TYPE', self.create_content_type)
        self.content_length = self.environ_parse('CONTENT_LENGTH', int)
        self.server_name = self.environ_parse('SERVER_NAME', str)
        self.server_port = self.environ_parse('SERVER_PORT', int)

    def environ_parse(self, key, a_callable):
        """
        Parse an item from the WSGI environment given a key. Return the 
        result of a_callable(environ.get(key)).
        """
        if key in self.environ:
            return a_callable(self.environ[key])

    def create_filelike(self, to_be_wrapped):
        """
        Wrap a pythonic file-like object in a helper class.
        @param to_be_wrapped: A file-like object to be wrapped by this class
        """
        return Filelike(self.config, to_be_wrapped)

    def create_content_type(self, to_be_wrapped):
        """
        Wrap a content-type string in a helper class.
        @param to_be_wrapped: A content-type string to be wrapped by this class
        """
        return ContentType(self.config, to_be_wrapped)

    def input_stream(self):
        """
        Current functionality: return self.wsgi_input
        Future functionality:
            Get the body of this HTTP request as a stream. This function 
            should be sure and only store an appropriate amount of data 
            in memory.

            Use this method unless you want the original ``wsgi.input`` 
            from self.environ.
        """
        return self.wsgi_input

    def input_string(self):
        """
        Get the entire body of this request and return it as a string.
        """
        return str(self.wsgi_input.read())

    def input_dict(self, allow_multiple_values = False):
        """
        Get this request as a dictionary object. Typically for GET requests, 
        this will be a dictionary of the query string parameters. Typically
        for POST and PUT requests, this will be a dictionary of form data.

        @param allow_multiple_values: If True, values can be lists if a
            key is encountered more than once.
        """
        data = defaultdict(list())
        data.update(parse_qs(self.query_string or ""))

        if self.content_type.is_form():
            data.update(parse_qs(self.input_string()))

        if not allow_multiple_values:
            for item in data.values():
                item = item[0]

        return data

import unittest
from wsgiref.util import setup_testing_defaults
from ConfigParser import ConfigParser

class TestRequest(unittest.TestCase):
    """
    Class to test all functionality of the Request class.
    """
    
    def setUp(self):
        """
        Load test configurations and WSGI environments.
        """
        self.config = ConfigParser()
        self.environ = {}
        
        setup_testing_defaults(self.environ)
    
    def test_basic_request(self):
        """
        A basic request can be made.
        """
        r = Request(self.config, self.environ)
        self.assertTrue(r)

if __name__ == "__main__":
    unittest.main()

