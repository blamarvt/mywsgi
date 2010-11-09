"""
contenttype.py
"""

class ContentType(object):
    """
    Object to represent the simple complexities of a "Content-Type" string.
    """
    
    def __init__(self, config, content_type_string):
        """
        Create a ContentType from a standard ConfigParser config
        and a content_type_string from a WSGI environment.
        """
        self.config = config
        self.mimetype = content_type_string.split(";")[0]

    def is_form(self):
        """
        Return true if mimetype is consistent with form data. Unsure
        what to call this function other than is_form because this 
        function *explicitly* does not return true for `multipart/form-data`
        mimetypes.
        """
        return self.mimetype == "application/x-www-form-urlencoded"
