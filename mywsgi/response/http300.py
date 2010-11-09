"""
300.py
"""

import httplib

from .base import Response

class MultipleChoicesResponse(Response):
    """
    300 Multiple Choices
    """

    status_code = httplib.MULTIPLE_CHOICES


class MovedPermanentlyResponse(Response):
    """
    301 Moved Permanently
    """

    status_code = httplib.MOVED_PERMANENTLY


class FoundResponse(Response):
    """
    302 Found
    """
    
    status_code = httplib.FOUND


class SeeOtherResponse(Response):
    """
    303 See Other
    """
    
    status_code = httplib.SEE_OTHER


class NotModifiedResponse(Response):
    """
    304 Not Modified
    """
    
    status_code = httplib.NOT_MODIFIED


class UseProxyResponse(Response):
    """
    305 Use Proxy
    """
    
    status_code = httplib.USE_PROXY


class TemporaryRedirectResponse(Response):
    """
    306 Temporary Redirect
    """
    
    status_code = httplib.TEMPORARY_REDIRECT

