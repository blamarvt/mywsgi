#!/usr/bin/env python
#
# Copyright 2010 Brian Lamar
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
mywsgi.app.base
"""

import traceback

import mywsgi.util.exceptions as exceptions

from mywsgi.request import Request
from mywsgi.response import Response, WsgiException
from mywsgi.util import Configuration

class Application(object):
    """
    All `mywsgi` projects must create a base `Application` to serve as the
    entry point for the system. The creation of an application requires
    a configuration to be passed in. This configuration will be shared 
    with all other relevant parts of the `mywsgi` system as needed.
 
    If a configuration is not passed it, all default will be used. When 
    defaults are used, logging should be utilized to make sure you are 
    aware of the default values.

    A simple `Application` might look like:

        my_application = Application()
    """

    request_class = Request
    response_class = Response
    next_steps = {}

    def __init__(self, config = None):
        """
        If no configuration is specified, make sure to log a warning. Even if
        a configuration is not specified at creation, one can be added while
        the application is running.
        """
        self.config = config or Configuration()
        self.logger = self.config.logger

    def __call__(self, environ, start_response):
        """
        All requests pass through here. No balrogs please.
        """
        self.environ = environ
        self.start_response = start_response

        try:
            if not self.is_active():
                raise WsgiException(503)

            request = self.create_request()
            response = self.execute(request)

        except WsgiException as ex:
            response = ex.response

        except Exception as ex:
            tb = traceback.format_exc()
            response = self.response_class(status = 500, content = tb)

        start_response(response.get_status(), response.get_wsgi_headers())
        return response.get_content()

    def is_active(self):
        """
        is_active : Is this dispatcher active? If no, all requests terminating 
                    at this dispatcher will return a 503 Service Unavailable
        """
        return self.config(self, "is_active", True, bool)

    def create_request(self):
        """
        Given a configuration and WSGI environment, return an
        instance of the class chosen to represent a request.
        """
        return self.request_class(self.config, self.environ)

    def next_step(self, request):
        """
        Retrieve the next step for this dispatcher.
        """
        next_step = request.consume()
        self.logger.debug("Next Step (string): %s" % next_step)

        if next_step is None:
            return None
        else:
            next_step = self.next_steps.get(next_step)
            self.logger.debug("Next Step (from dispatcher): %r" % next_step)
            self.logger.debug("Dispatcher: %s" % self.next_steps)
            try:
                return next_step(self.environ, self.start_response) 
            except TypeError:
                raise WsgiException(404)

    def execute(self, request):
        """
        Execute the function corresponding to the method given.
        """
        next_step = self.next_step(request)
        if next_step is not None:
            self.logger.debug("Next step found. (%r)" % next_step)
            return next_step(request)

        known_methods = ['GET','PUT','POST','DELETE','HEAD','OPTIONS','TRACE','CONNECT']
        method_name = "handle_%s" % request.method.lower()

        self.logger.debug("Calling %s on %r" % (method_name, self))

        try:
            method = getattr(self, method_name)
        except AttributeError:
            if request.method.lower() in known_methods:
                return WsgiException(405)
            else:
                return WsgiException(501)

        return method(request)

    def serve_foreground(self):
        """
        Serve this application via a WSGI server on the console.
        """
        from gevent import pywsgi
        pywsgi.WSGIServer(('0.0.0.0', 8080), self).serve_forever()
