"""
test_response.py
"""

import unittest

from mywsgi.util.config import Config
from mywsgi.response import Response

class TestResponse(unittest.TestCase):
    """
    Class to test all functionality of the Response class.
    """
    
    def setUp(self):
        """
        Load test configurations and WSGI environments.
        """
        self.config = Config()
    
    def test_basic_response(self):
        """
        A basic response can be made.
        """
        r = Response(self.config)
        self.assertTrue(r)
