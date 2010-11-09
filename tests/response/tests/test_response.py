"""
test_response.py
"""

import unittest
from pprint import pprint
from ConfigParser import ConfigParser

from mywsgi.view import View
from mywsgi.response import Response

class TestResponse(unittest.TestCase):
    """
    Class to test all functionality of the Response class.
    """
    
    def setUp(self):
        """
        Load test configurations and WSGI environments.
        """
        self.config = ConfigParser()
        self.view = View()
    
    def test_basic_response(self):
        """
        A basic response can be made.
        """
        r = Response(self.config, self.view)
        self.assertTrue(r)
