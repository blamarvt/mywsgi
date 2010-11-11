"""
test_response.py
"""

import unittest

from mywsgi.util import Configuration
from mywsgi.response import Response

class TestResponse(unittest.TestCase):
    """
    Class to test all functionality of the Response class.
    """
    
    def setUp(self):
        """
        Load test configurations and WSGI environments.
        """
        self.config = Configuration()
    
    def test_basic_response(self):
        """
        A basic response cannot be made.
        """
        self.assertRaises(Exception, Response)
