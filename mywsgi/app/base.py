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
from mywsgi.response import Response
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

    def __init__(self, config = None):
        """
        If no configuration is specified, make sure to log a warning. Even if
        a configuration is not specified at creation, one can be added while
        the application is running.
        """
        self.config = config or Configuration()

    def __call__(self, environ, start_response):
        """
        All requests pass through here. No balrogs please.
        """
        self.environ = environ
        self.start_response = start_response

        try:
            if not self.is_active():
                raise exceptions.ServiceUnavailableResponse()

            request = self.create_request()
            response = self.execute(request)

        except WsgiException as ex:
            response = ex

        except Exception as ex:
            tb = traceback.format_exc()
            response = self.response_class(status_code = 500, content = tb)

        return response.respond()

    def is_active(self):
        """
        is_active : Is this dispatcher active? If no, all requests terminating 
                    at this dispatcher will return a 503 Service Unavailable
        """
        self.is_active = self.config(self, "is_active", True, bool)

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
        next_step = request.consume_script_name()
        if next_step is None or self.next_steps.get(next_step) is None:
            return None
        else:
            return self.next_steps.get(next_step)(self.environ, self.start_response)

    def execute(self, request):
        """
        Execute the function corresponding to the method given.
        """
        next_step = self.next_step(request)
        if next_step is not None:
            return next_step(request)

        known_methods = ['GET','PUT','POST','DELETE','HEAD','OPTIONS','TRACE','CONNECT']
        method_name = "handle_%s" % request.method.lower()

        try:
            method = getattr(self, method_name)
        except AttributeError:
            if request.method.lower() in known_methods:
                return exceptions.MethodNotAllowedResponse()
            else:
                return exceptions.NotImplementedResponse()

        return method(request)
