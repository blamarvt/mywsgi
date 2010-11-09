"""
base.py
"""

import traceback

import mywsgi.util.exceptions as exceptions

from mywsgi.request import Request
from mywsgi.response import Response

__config_section__ = "mywsgi:application"

class WsgiApplication(object):
    """
    Simple WSGI application which utilizes Request and Response
    objects to correctly handle incomming traffic.
    """

    request_class = Request
    response_class = Response

    def __init__(self, config):
        """
        Initialize a new WSGI application.
        """
        self.config = config

        # Is this application active? If not, all requests return a 503
        self.is_active = self.config(__config_section__, "active", True, bool)

    def __call__(self, environ, start_response):
        """
        All requests enter here. No balrogs please.
        """
        try:
            method = environ["REQUEST_METHOD"]

            if not self.is_active:
                raise exceptions.ServiceUnavailable()

            if self. is None or self.routes.get(method) is None:
                raise exceptions.NotImplemented()

            # TODO: Handle 414 check
            # TODO: Handle 400 check
            request = self.create_request(config, environ)

            # TODO: Handle 405 check
            router = self.create_router(config)

            response = router.route(request)

            return response.success()

        except exceptions.WsgiException as ex:
            response = self.create_response(self.config, self.environ)
            return response.error(ex)

        except Exception:
            response = self.create_response(self.config, self.environ)
            return response.generic_error()

    def create_request(config, environ):
        """
        Given a configuration and WSGI environment, return an
        instance of the class chosen to represent a request.
        """
        return self.request_class(config, environ)

    def create_response(config, environ):
        """
        Given a configuration and WSGI environment, return an
        instance of the class chosen to represent a response.
        """
        return self.response_class(config, environ)

    def create_router(config):
        """
        Create a WSGI Router class from the config given.
        """
        return self.router_class(config)
