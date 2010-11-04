"""
__init__.py provides:
    1) Module initialization for mywsgi.request
    2) Common functions needed by mywsgi.request
"""

def html_escape(s):
    """
    HTML-escape a string or object.

    Convert a non-string object into a strings. All values returned are
    non-unicode strings (using `&#num;` entities for all non-ASCII characters).

    None is treated specially, and returns the empty string.
    """
    if s is None:
        return ''
    if hasattr(s, '__html__'):
        return s.__html__()
    if not isinstance(s, basestring):
        if hasattr(s, '__unicode__'):
            s = unicode(s)
        else:
            s = str(s)
    s = cgi.escape(s, True)
    if isinstance(s, unicode):
        s = s.encode('ascii', 'xmlcharrefreplace')
    return s
