"""
Pythonic daemon using daemonhelper library and gevent.pywsgi.
"""

from gevent import pywsgi
from daemonhelper import GeventDaemon, make_main

from mywsgi.util import MyWsgiApplication

class MyWsgiDaemon(GeventDaemon):
    """
    Daemon which wraps a MyWsgiApplication to provide configuration,
    logging, and ... a daemon.
    """

    name = "mywsgi"

    def __init__(self):
        """
        Initialize the management daemon.
        """
        GeventDaemon.__init__(self)

        # WSGI configuration from /etc/<name>.conf
        host = self.config("server", "host", "0.0.0.0", str)
        port = self.config("server", "port", 80, int)

        # Set up logging
        log_level = self.config("logging", "level", 10, int)
        self.logger.setLevel(log_level)

        # Create WSGI server
        self.application = WsgiApplication(self.logger, self.config)

    def handle_run(self):
        """
        Logic for starting the DMS management daemon.
        """
        self.application.start()

    def handle_stop(self):
        """
        Logic for stopping the DMS management daemon.
        """
        self.application.stop()

main = make_main(MyWsgiDaemon)
