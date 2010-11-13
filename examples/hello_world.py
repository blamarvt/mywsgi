"""
hello_world.py
"""

from mywsgi.app import Application
from mywsgi.response import PlainTextResponse

class HelloWorldApp(Application):
    """
    Very simple request handler which has functions such as `handle_get`, 
    `handle_post`, `handle_put`, and `handle_delete` which can be defined 
    to return data.
    """

    def handle_get(self, request):
        """
        GET / is handled here.
        """
        return PlainTextResponse("Hello World")

root_app = Application()
step_one = Application()
step_two = Application()
hello_world = Application()

root_app.next_steps = {
    "hello" : step_one
}

step_one.next_steps = {
    "world" : step_two
}

step_two.next_steps = {
    "nick" : hello_world
}

if __name__ == "__main__":
    root_app.serve_foreground()
