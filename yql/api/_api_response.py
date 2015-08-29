from ._api_mapper import ObjectMapper
import json
import six


class _Api_Response(object):

    '''A class that takes the request object as input
       and converts into the response of yql api.
    '''

    def __init__(self, response, type="json"):

        self.status = response.status_code
        if type == "json":
            if six.PY3:
                self._object = ObjectMapper(json.loads(response.content.decode()))
            else:
                self._object = ObjectMapper(json.loads(response.content))
        else:
            self._object = response.content

    @property
    def result(self):
        '''Returns the Mapped Object

        Returns:
          _object(object): Mapped Object
        '''
        return self._object
