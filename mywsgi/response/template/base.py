"""
base.py
"""

__config_section__ = "mywsgi.response.template"

class Template(object):
    """
    Template
    """

    def __init__(self, config):
        """
        @param config: A mywsgi.util.config object
        """
        self.config = config

    def render(self):
        """
        Render unto the template what is the template's.
        """
        pass
