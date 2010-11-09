"""
filelike.py
"""

class Filelike(object):
    """
    Wrap a file-like object and provide
    additional functionality.
    """

    def __init__(self, config, to_be_wrapped):
        """
        Take in a standard ConfigParser config and a file-like
        object and create a Filelike instance.
        """
        self.config = config
        self.raw_file = to_be_wrapped

