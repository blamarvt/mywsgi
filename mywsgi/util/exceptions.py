"""
exceptions.py
"""

class MyException(Exception):
    """
    MyException
    """

    def __init__(self, **kwargs):
        """
        Extend `Exception` to provide a message.
        """
        Exception.__init__(self)
        self.values = kwargs

        if self.__class__ is MyException:
            raise Exception()
    
    def show(self):
        """
        Dictionary replace the message.
        """
        return self.message % (self.values)


class AbstractClassException(MyException):
    """
    AbstractClassException
    """
    
    message = "'%(cls)s' is an abstract class, and may not be implemented."
