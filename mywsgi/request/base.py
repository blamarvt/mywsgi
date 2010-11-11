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
mywsgi.request
"""

import logging
import urlparse

from collections import defaultdict

from mywsgi.util.url import Url
from mywsgi.util.filelike import Filelike
from mywsgi.util.contenttype import ContentType

class Request(object):
    """
    Request Object
    """

    url_class = Url
    filelike_class = Filelike
    content_type_class = ContentType

    def __init__(self, config, environ):
        """
        Given a configuration object and a WSGI compliant environ,
        create a Request class instance.
        """
        self.config = config
        self.environ = environ

        self._load_pep333_headers()
        self._load_random_headers()
        
        self.url = self.create_url()
        self.content_type = self.content_type or self.detect_content_type()

    def _load_pep333_headers(self):
        """
        Get known WSGI variables (PEP333)
        """
        self.wsgi_version = self.environ_parse('wsgi.version', tuple)
        self.wsgi_scheme = self.environ_parse('wsgi.url_scheme', str)
        self.wsgi_input = self.environ_parse('wsgi.input', self.create_filelike)
        self.wsgi_errors = self.environ_parse('wsgi.errors', self.create_filelike)
        self.wsgi_multithread = self.environ_parse('wsgi.multithread', bool)
        self.wsgi_multiprocess = self.environ_parse('wsgi.multiprocess', bool)
        self.wsgi_runonce = self.environ_parse('wsgi.run_once', bool)
        self.method = self.environ_parse('REQUEST_METHOD', str)
        self.script_name = self.environ_parse('SCRIPT_NAME', str)
        self.path_info = self.environ_parse('PATH_INFO', str)
        self.query_string = self.environ_parse('QUERY_STRING', str)
        self.content_type = self.environ_parse('CONTENT_TYPE', self.create_content_type)
        self.content_length = self.environ_parse('CONTENT_LENGTH', int)
        self.server_name = self.environ_parse('SERVER_NAME', str)
        self.server_port = self.environ_parse('SERVER_PORT', int)

    def _load_random_headers(self):
        """
        Get 'random' HTTP_ headers from the WSGI environ.
        """
        for key, value in self.environ.items():
            if key.startswith("HTTP_"):
                header = key.lower()[5:]
                if not hasattr(self, header):
                    setattr(self, header, value)
                else:
                    logging.warn("%s header set, but request.%s already exists.", key, header)

    def environ_parse(self, key, a_callable):
        """
        Parse an item from the WSGI environment given a key. Return the 
        result of a_callable(environ.get(key)).
        """
        if key in self.environ:
            return a_callable(self.environ[key])

    def create_filelike(self, to_be_wrapped):
        """
        Wrap a pythonic file-like object in a helper class.
        @param to_be_wrapped: A file-like object to be wrapped by this class
        """
        return self.filelike_class(self.config, to_be_wrapped)

    def create_content_type(self, to_be_wrapped):
        """
        Wrap a content-type string in a helper class.
        @param to_be_wrapped: A content-type string to be wrapped by this class
        """
        return self.content_type_class(self.config, to_be_wrapped)

    def create_url(self):
        """
        Instantiate the WSGI Url class defined by self.url_class.
        """
        return self.url_class(self.config, self.wsgi_scheme, self.server_name,
            self.server_port, self.script_name, self.path_info, self.query_string)

    def detect_content_type(self):
        """
        This function should only be called if no content-type header 
        is passed to us. Attempt detection of a content-type and if we
        can't do that, just return "application/octet-stream".
        """
        return self.create_content_type("application/octet-stream")

    def input_stream(self):
        """
        Current functionality: return self.wsgi_input
        Future functionality:
            Get the body of this HTTP request as a stream. This function 
            should be sure and only store an appropriate amount of data 
            in memory.

            Use this method unless you want the original ``wsgi.input`` 
            from self.environ.
        """
        return self.wsgi_input

    def input_string(self):
        """
        Get the entire body of this request and return it as a string.
        """
        return str(self.wsgi_input.read())

    def input_dict(self, allow_multiple_values = False):
        """
        Get this request as a dictionary object. Typically for GET requests, 
        this will be a dictionary of the query string parameters. Typically
        for POST and PUT requests, this will be a dictionary of form data.

        @param allow_multiple_values: If True, values can be lists if a
            key is encountered more than once.
        """
        data = defaultdict(list)
        data.update(urlparse.parse_qs(self.query_string or ""))

        if self.content_type.is_urlencoded_form():
            for key, value_list in urlparse.parse_qs(self.input_string() or "").items():
                for value in value_list:
                    data[key].append(value)

        if not allow_multiple_values:
            for item in data.values():
                item = item[0]

        return data
