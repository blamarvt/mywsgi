"""
route.py

Classes contained within this file deal with "routes".
"""

class Route(object):
    """
    A route is a combination of a PATH, METHOD, and a CALLBACK. 
    For example, a simplified route might be something like this:

    self.routes = [
        ('GET',  '/', MainPage),
        ('POST', '/', MainPage),
        ('PUT',  '/', MainPage)
    ]
    """

    def __init__(self, path, schema, method = "GET"):
        """
        @param path: The path which belongs to this route
        @param callback: The callback to execute
        @param method: GET | POST | PUT | DELETE | HEAD | OPTIONS
        """
        self.path = path
        self.schema = schema
        self.method = method

    def execute(self, request):
        """
        Execute this route, which entails quite a bit.
        """
        request.check_authorization(schema)
