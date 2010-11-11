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
mywsgi.response
"""

import httplib

from mywsgi.util.exceptions import AbstractClassException

class Response(object):
    """
    Base class for all responses in the `mywsgi` framework.
    """

    def __init__(self, status, content = None, headers = None):
        """
        @param status: An HTTP status integer
        @param content: A string, iterator, or file-like object
        @param headers: A list of tuples (header_name, value)
        """
        self.status = status
        self.content = content
        self.headers = headers
        
        if self.__class__ is Response:
            raise AbstractClassException(cls = self.__class__)

    def get_content(self):
        """
        Retrieve the content, use for overriding in subclasses.
        """
        return self.content

    def set_content(self, value):
        """
        Set the content for this response.
        """
        self._content = value or ""

    def get_headers(self):
        """
        Retrieve the response headers.
        """
        return self.headers

    def set_headers(self, value):
        """
        Set the headers for this response.
        """
        self._headers = value or []

    def get_status(self):
        """
        Retrieve the HTTP status message for this response.
        (e.g. 200 OK, 403 Forbidden, 500 Internal Server Error)
        """
        return "%d %s" % (self.status, httplib.responses[self.status])

    def set_status(self, value):
        """
        Set the status code for this resposne.
        """
        self._status = value or 200

    def get_content_type(self):
        """
        Get the response's Content-Type header.
        """
        return self.headers["Content-Type"] or "text/plain"

    def set_content_type(self, value):
        """
        Set the response's Content-Type header.
        """
        self.headers["Content-Type"] = value

    status = property(get_status, set_status)
    content = property(get_content, set_content)
    headers = property(get_headers, set_headers)
    content_type = property(get_content_type, set_content_type)
