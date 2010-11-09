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

    def is_urlencoded_form(self):
        """
        Return true if mimetype is consistent with simple form data. 
        """
        return self.mimetype == "application/x-www-form-urlencoded"

    def is_multipart_form(self):
        """
        Return true if mimetype is consistent with `multiple/form-data`.
        """
        return self.mimetype == "multipart/form-data"

    def is_form(self):
        """
        Helper function for determining if this content-type is from a form.
        """
        return self.is_urlencoded_form() or self.is_multipart_form()
