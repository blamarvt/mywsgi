"""
Example of a WSGI handler.
"""

import re
import traceback
from collections import defaultdict

from mywsgi.request import Request
from mywsgi.templates import ErrorTemplate
from mywsgi.exceptions import *

class WsgiHandler(object):
    """
    Generic WSGI handler.
    """

    routes = defaultdict(dict)

    def __init__(self, logger, config):
        """
        Initialize a new WSGI handler.
        """
        self.logger = logger
        self.config = config

        # Is this service active? If not, all requests return a 503
        self.is_active = self.config("wsgi", "active", True, bool)

        # Should we show errors when unexpected errors arise?
        self.show_errors = self.config("wsgi", "show_errors", False, bool)
        self.error_template = ErrorTemplate(show_errors=self.show_errors)

        # Specify a maximum URI length for safety!
        self.max_uri = self.config("wsgi", "max_uri", 1024, int)

    def __call__(self, environ, start_response):
        """
        Every request to the WSGI service comes through here.
        """
        try:
            method = environ["REQUEST_METHOD"]

            if not self.is_active:
                raise ServiceUnavailable()

            if self.routes is None or self.routes.get(method) is None:
                raise NotImplemented()

            # Handle 414 check
            # Handle 400 check
            request = Request(environ)

            # Handle 405 check
            route = self.choose_route(request.method, request.path)

            # Continue down the rabbit hole...
            response = route.execute(request)

        except WsgiException as ex:
            start_response(ex.status(), ex.headers)
            return ex.content

        except Exception:
            tb = traceback.format_exc()
            self.logger.error(tb)
            start_response("500 Internal Server Error", self.error_template.headers)
            return self.error_template.render(tb=tb)

    def choose_route(method, path):
        """
        Choose a route by testing the list of routes
        for one that matches. If multiple match, then
        we have to somehow choose the best one.
        """
        matches = []
        for route in self.routes[method].values():
            if route.match(path):
                matches.append(route)

        # Sort the results, which sorts the Routes by "confidence"
        sort(matches)

        if matches:
            return matches[0]
        else:
            raise MethodNotAllowed()
