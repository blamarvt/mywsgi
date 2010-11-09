"""
http200.py
"""

import httplib

from .base import Response

class OkayResponse(Response):
    """
    200 OK
    """

    status_code = httplib.OK


class CreatedResponse(Response):
    """
    201 Created
    """

    status_code = httplib.CREATED


class AcceptedResponse(Response):
    """
    202 Accepted
    """
    
    status_code = httplib.ACCEPTED


class NonAuthoritativeInformationResponse(Response):
    """
    203 Non Authoritative Information
    """
    
    status_code = httplib.NON_AUTHORITATIVE_INFORMATION


class NoContentResponse(Response):
    """
    204 No Content
    """
    
    status_code = httplib.NO_CONTENT

    def __call__(self, content, headers):
        """
        Overridden __call__ to ensure content is never passed.
        """
        Response.__call__(self, None, headers)


class ResetContentResponse(Response):
    """
    205 Reset Content
    """
    
    status_code = httplib.RESET_CONTENT


class PartialContentResponse(Response):
    """
    206 Partial Content
    """
    
    status_code = httplib.PARTIAL_CONTENT

