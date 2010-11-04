"""
responses.py

Most, if not all, content is returned through the use of custom classes.
"""

import httplib

class WsgiResponse(object):
    """
    Generic WSGI response class which serves to output data
    given to it by objects which conform to the FlexibleObject
    interface.
    """

    def __init__(self, request, schema, ):
        """
        Creation of a WsgiResponse requires a valid HTTP code and a
        valid mywsgi.Request object. Optional content can be passed
        which will be the body of the response.
        """
        # Can we process this Accept header successfully?
        if request.accept and not schema.accept(request.accept):
            raise NotAcceptable(request)

        # Can we process this Accept-Language header successfully?
        if request.accept_language and not schema.accept_language(request.accept_language):
            raise NotAcceptable(request)

        # Can we process this Accept-Charset header successfully?
        if request.accept_charset and not schema.accept_charset(request.accept_charset):
            raise NotAcceptable(request)

        # Can we process this Accept-Encoding header successfully?
        if request.accept_encoding and not schema.accept_encoding(request.accept_encoding):
            raise NotAcceptable(request)
        

        self.content = content or "%d %s" % (self.code, httplib.responses[self.code])
        self.request = request
        self.headers = []

    def __repr__(self):
        """
        East to read representation of the response.
        """
        return "<%s status=%s>" % (self.__class__.__name__, self.status())

    def status(self):
        """
        Return useful status information (e.g. 404 Not Found)
        """
        return "%d %s" % (self.code, httplib.responses[self.code])


class FlexibleContent(WsgiResponse):
    """
    Flexible content class which will morph a data-model instance
    into the content desired by the client.
    """

    def __init__(self, request, content = None):
        """
        Encode and return the content with a 
        responsible content type.
        """
        WsgiResponse.__init__(self, request)
        
        for mimetype in request.prioritized_types:
            if content.supports_type(mimetype):
                self.code = httplib.OK
                self.headers.content_type = mimetype
                self.content = content.serialize_as(mimetype)

        # If we don't have any content from the content-type
        # negotiation above, then return a 406 Not Acceptable
        # with a text/plain content type as a fallback.
        if elf.headers.content_type is None:
            self.code = httplib.NOT_ACCEPTABLE
            self.headers.content_type = 'text/plain'
            self.content = ""

class StaticContent(WsgiResponse):
    """
    Static file
    """

    code = httplib.OK
    content_type = None
    last_modified = None
    date_format = "%a, %d %b %Y %H:%M:%S GMT"

    def __init__(self, request, path):
        """
        Populate content with path data
        """
        import os
        import time
        import mimetypes

        if not os.path.exists(path):
            raise NotFound(request)

        if not os.access(path, os.R_OK):
            raise Forbidden(request)

        self.content_type = mimetypes.guess_type(path)[0]
        last_modified = time.gmtime(os.stat(path).st_mtime)
        self.last_modified = time.strftime(self.date_format, last_modified)

        self.code = httplib.OK
        self.headers = [
            ('Content-Type', self.content_type),
            ('Last-Modified', self.last_modified)
        ]
        self.content = open(path)
# }}}
# HTTP 204 No Content {{{
class NoContent(WsgiResponse):
    """
    204 No Content
    """

    code = httplib.NO_CONTENT
# }}}
# HTTP 303 See Other {{{
class Redirect(WsgiResponse):
    """
    303 See Other
    """
    
    code = httplib.SEE_OTHER

    def __init__(self, request, location):
        """
        Redirect
        """
        WsgiResponse.__init__(self, request)
        self.location = location
        self.headers = [("Location", self.location)]
# }}}
# HTTP 400 Bad Request {{{
class BadRequest(WsgiResponse):
    """
    400 Bad Request
    """

    code = httplib.BAD_REQUEST
# }}}
# HTTP 403 Forbidden {{{
class Forbidden(WsgiResponse):
    """
    403 Forbidden
    """

    code = httplib.FORBIDDEN
# }}}
# HTTP 404 Not Found {{{
class NotFound(WsgiResponse):
    """
    404 Not Found response
    """

    code = httplib.NOT_FOUND
# }}}
# HTTP 414 Request URI Too Long {{{
class UriTooLong(WsgiResponse):
    """
    414 Request URI too long
    """

    code = httplib.REQUEST_URI_TOO_LONG
# }}}
# HTTP 501 Not Implemented {{{
class NotImplemented(WsgiResponse):
    """
    501 Not Implemented response
    """

    code = httplib.NOT_IMPLEMENTED
# }}}
