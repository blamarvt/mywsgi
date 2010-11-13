"""
test_request.py
"""

import unittest

from wsgiref import util

from mywsgi.request import Request
from mywsgi.util.config import Configuration
from mywsgi.util.contenttype import ContentType

class TestRequest(unittest.TestCase):
    """
    Class to test all functionality of the Request class.
    """
    
    def setUp(self):
        """
        Load test configurations and WSGI environments.
        """
        self.config = Configuration()
        self.environ = {}

        # Setup faux WSGI environment
        util.setup_testing_defaults(self.environ)
    
    def test_basic_request(self):
        """
        A basic request can be made.
        """
        r = Request(self.config, self.environ)
        self.assertTrue(r)

    def test_content_type(self):
        """
        Test our content-type string is returned as a ContentType
        class instance.
        """
        r = Request(self.config, self.environ)
        self.assertEquals("application/octet-stream", r.content_type.mimetype)

    def test_input_dict(self):
        """
        Test what sort of information you get from input_dict
        when using a really basic environment.
        """
        r = Request(self.config, self.environ)
        self.assertEquals({}, r.input_dict())

    def test_full_url(self):
        """
        Test the concatenating of everything together for form
        a full URL representation.
        """
        r = Request(self.config, self.environ)
        self.assertEquals("http://127.0.0.1:80/", str(r.url))

    def test_query_string_dict(self):
        """
        Test parse of a query string.
        """
        self.environ['QUERY_STRING'] = "asdf=123&abd=def"
        r = Request(self.config, self.environ)
        self.assertEquals({"asdf":"123","abd":"def"}, r.input_dict())
