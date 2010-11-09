"""
400.py
"""

import httplib

from mywsgi.response import Response

class BadRequestResponse(Response):
    """
    400 Bad Request
    """

    status_code = httplib.BAD_REQUEST


class Unauthorizedesponse(Response):
    """
    401 Unauthorized
    """

    status_code = httplib.UNAUTHORIZED


class PaymentRequiredResponse(Response):
    """
    402 Payment Required
    """
    
    status_code = httplib.PAYMENT_REQUIRED


class ForbiddenResponse(Response):
    """
    403 Forbidden
    """
    
    status_code = httplib.FORBIDDEN


class NotFoundResponse(Response):
    """
    404 Not Found
    """
    
    status_code = httplib.NOT_FOUND


class MethodNotAllowedResponse(Response):
    """
    405 Method Not Allowed
    """
    
    status_code = httplib.METHOD_NOT_ALLOWED


class NotAcceptableResponse(Response):
    """
    406 Not Acceptable
    """
    
    status_code = httplib.NOT_ACCEPTABLE


class ProxyAuthenticationRequiredResponse(Response):
    """
    407 Proxy Authentication Required
    """
    
    status_code = httplib.PROXY_AUTHENTICATION_REQUIRED


class RequestTimeoutResponse(Response):
    """
    408 Request Timeout
    """
    
    status_code = httplib.REQUEST_TIMEOUT


class ConflictResponse(Response):
    """
    409 Conflict
    """
    
    status_code = httplib.CONFLICT


class GoneResponse(Response):
    """
    410 Gone
    """
    
    status_code = httplib.GONE


class LengthRequiredResponse(Response):
    """
    411 Length Required
    """
    
    status_code = httplib.LENGTH_REQUIRED


class PreconditionFailedResponse(Response):
    """
    412 Precondition Failed
    """
    
    status_code = httplib.PRECONDITION_FAILED


class RequestEntityTooLargeResponse(Response):
    """
    413 Request Entity Too Large
    """
    
    status_code = httplib.REQUEST_ENTITY_TOO_LARGE


class RequestUriTooLongResponse(Response):
    """
    414 Request URI Too Long
    """
    
    status_code = httplib.REQUEST_URI_TOO_LONG


class UnsupportedMediaTypeResponse(Response):
    """
    415 Unsupported Media Type
    """
    
    status_code = httplib.UNSUPPORTED_MEDIA_TYPE


class RequestRangeNotSatisfiableResponse(Response):
    """
    416 Request Range Not Satisfiable
    """
    
    status_code = httplib.REQUEST_RANGE_NOT_SATISFIABLE


class ExpectationFailedResponse(Response):
    """
    417 Expectation Failed
    """
    
    status_code = httplib.EXPECTATION_FAILED


