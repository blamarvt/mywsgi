"""
test_request.py
"""

import unittest
from pprint import pprint
from wsgiref import util
from ConfigParser import ConfigParser

from mywsgi.request import Request
from mywsgi.util.contenttype import ContentType

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
        self.assertEquals("application/octet-stream", self.content_type.mimetype)

    def test_input_dict(self):
        """
        Test what sort of information you get from input_dict
        when using a really basic environment.
        """
        r = Request(self.config, self.environ)
        self.assertEquals({}, r.input_dict())

    def test_full_uri(self):
        """
        Test the concatenating of everything together for form
        a full URI representation.
        """
        r = Request(self.config, self.environ)
        self.assertEquals({}, r.full_uri())
