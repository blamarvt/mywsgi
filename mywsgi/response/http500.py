"""
500.py
"""

import httplib

from .base import Response

class InternalServerErrorResponse(Response):
    """
    500 Internal Server Error
    """

    status_code = httplib.INTERNAL_SERVER_ERROR


class NotImplementedResponse(Response):
    """
    501 Not Implemented
    """

    status_code = httplib.NOT_IMPLEMENTED


class BadGatewayResponse(Response):
    """
    502 Bad Gateway
    """

    status_code = httplib.BAD_GATEWAY


class ServiceUnavailableResponse(Response):
    """
    503 Service Unavailable
    """

    status_code = httplib.SERVICE_UNAVAILABLE


class GatewayTimeoutResponse(Response):
    """
    504 Gateway Timeout
    """

    status_code = httplib.GATEWAY_TIMEOUT


class HttpVersionNotSupportedResponse(Response):
    """
    505 Http Version Not Supported
    """

    status_code = httplib.HTTP_VERSION_NOT_SUPPORTED


