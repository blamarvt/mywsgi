"""
json.py
"""

import httplib
import simplejson as json

class JsonResponse(object):
    """
    Base class for all responses in the `mywsgi` framework.
    """

    status_code = httplib.OK

    def get_content(self):
        """
        Retrieve the content of this response in JSON format.
        """
        return json.dumps(self.content)
