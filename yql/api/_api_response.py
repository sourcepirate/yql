from ._api_mapper import ObjectMapper


class _Api_Response(object):

    '''A class that takes the request object as input
       and converts into the response of yql api.
    '''

    def __init__(self, response, *args,  **kwargs):

        self.status = response.status_code
        self._object = ObjectMapper(response.content)

    @property
    def result(self):
        '''Returns the Mapped Object

        Returns:
          _object(object): Mapped Object
        '''
        return self._object
