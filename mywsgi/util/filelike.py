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

    def stream(self):
        """
        Return the file-like. In the future this might rate limit the
        file or buffer/chunk intelligently.
        """
        return self.raw_file

    def get(self):
        """
        Return the contents of the file-like. In the future this might
        rate limit the file, make a temp file, buffer, etc.
        """
        return self.raw_file.read()
