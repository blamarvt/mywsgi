"""
hello_world.py
"""

from mywsgi.application import Application
from mywsgi.response import PlainTextResponse
from mywsgi.request import RequestHandler, RegexRouter

class ExampleHandler(RequestHandler):
    """
    Very simple request handler which has functions such as `handle_get`, 
    `handle_post`, `handle_put`, and `handle_delete` which can be defined 
    to return data.
    """

    route = RegexRouter.routing_decorator()

    @route(r"/")
    def handle_get(self):
        """
        RequestHandlers provide function such as self.write() and 
        self.finish() to write data to the HTTP stream.
        """
        return PlainTextResponse("Hello World")


if __name__ == "__main__":
    Application(ExampleHandler).run()
