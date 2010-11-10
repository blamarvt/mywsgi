"""
url.py
"""

__config_section__ = "mywsgi.util.url"

class Url(object):
    """
    Url
    """

    def __init__(self, config, scheme, host, port, script, path, query_string):
        """
        @param config: A wsgi.util.config object
        @param scheme: The WSGI scheme (normally http or https)
        @param host: The host requested
        @param port: The port requested
        @param script: The WSGI SCRIPT_NAME
        @param path: The WSGI PATH_INFO
        @param qs: The query string
        """
        self.config = config
        self.scheme = scheme
        self.host = host
        self.port = port
        self.script = script
        self.path = path
        self.query_string = query_string

        self.full_url = "%s://%s:%d%s" % (self.scheme, self.host, self.port, self.script)

        if self.path:
            self.full_url += self.path

        if self.query_string:
            self.full_url += "?%s" % self.query_string

    def __str__(self):
        """
        Represent the URL as a string.
        """
        return self.full_url
