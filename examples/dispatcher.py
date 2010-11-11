"""
dispatcher.py

For this example, our application will handle serializing a string
into different content types depending on the URL requested.

This example will run in the foreground with a small amount of logging.

To run:
    $ python dispatcher.py
"""

from mywsgi.response import JsonResponse, XmlResponse, PlainTextResponse
from mywsgi.dispatcher import Dispatcher

CONTENT = "Hello World!" # This is the string which will be returned

class RootDispatcher(Dispatcher):
    """
    All requests flow through this dispatcher to other dispatchers.
    """
    
    def __init__(self):
        """
        Define next stypes for this dispatcher.
        """
        RootDispatcher.__init__(self)

        self.dispatch = {
            "json" : JsonDispatcher,
            "xml"  : XmlDispatcher,
        }
        self.default_dispatcher = PlainTextDispatcher


class JsonDispatcher(Dispatcher):
    """
    Returns "Hello World!" in application/json
    """
    
    def handle_get(self, request):
        """
        Called on GET of /json
        """
        return JsonResponse(content = CONTENT)


class XmlDispatcher(Dispatcher):
    """
    Returns "Hello World!" in application/xml
    """
    
    def handle_get(self, request):
        """
        Called on GET of /xml
        """
        return XmlResponse(content = CONTENT)


class PlainTextDispatcher(Dispatcher):
    """
    Returns "Hello World!" in text/plain
    """

    def handle_get(self, request):
        """
        Called on GET of anything we haven't specified above.
        """
        return PlainTextResponse(content = CONTENT)


if __name__ == "__main__":
    root = RootDispatcher()
    root.foreground()
    #root.daemonize()
