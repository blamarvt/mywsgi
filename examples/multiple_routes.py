"""
multiple_routes.py
"""

from mywsgi.application import Application
from mywsgi.response import PlainTextResponse, JsonResponse
from mywsgi.request import RequestHandler, Router

class ExampleHandler(RequestHandler):
    """
    Simple handler which allows for a function per page.
    """

    def handle_index(self, request):
        """
        Choose from a number of Response classes to return your data.
        """
        return PlainTextResponse("This is the index!")

    def handle_another_page(self, request):
        """
        Handle some other page!
        """
        return JsonResponse("This will be in JSON")


class ExampleRouter(Router):
    """
    Route incomming requests to their correct handlers.
    """

    def __init__(self):
        """
        Initialize needed handlers for this router.
        """
        self.my_handler = ExampleHandler()
    
    def route(self, request, url):
        """
        Called on each request with a URL object which represents
        the currect request.
        """
        if url.path == "/":
            result = self.my_handler.handle_index(request)
        else
            result = self.my_handler.handl_another_page(request)

        return result

if __name__ == "__main__":
    Application(router=ExampleRouter).run()
