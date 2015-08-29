
from requests import Session
from yql._builder import _YQLBuilder
from ._api_response import _Api_Response
from six.moves.urllib.parse import urlencode
import json

_yahoo_api = 'https://query.yahooapis.com/v1/public/yql'

class _Api_Request(Session):

    '''
    A new Request of object for creating a
    new api session object.

    '''

    def __init__(self, *args, **kwargs):
        """

         Object block consistes of a table name
         and builder get initialised for constructing
         the quries.

        """

        self.__tablename = kwargs.pop('table', None)
        self.__yql = _YQLBuilder(self.__tablename)
        super(_Api_Request, self).__init__(*args, **kwargs)


    def add_filter(self, name, value):
        '''Adds a filter on to the request

        Args:
           name(str): name of the yql column
           value(str, int, float): the value to which it should be matched against

        Returns:
           the current reference for chaining.
        '''
        self.__yql.filter(name, value)
        return self

    def get(self, column):
        '''Used to query the column on from tyql.

        Args:
           column(str): name of the column to query with particular filters

        if the get function is not invoked then it will query entire
        column "*" of yql.

        Returns:
          the current reference for chaining.

        '''

        self._yql.get(column)
        return self



    @property
    def result(self):
        url = self.__yql._construct()
        url = _yahoo_api+"?"+ urlencode(dict(q=url))
        response = super(_Api_Request, self).get(url)
        return _Api_Response(response)

    def json(self):
        url = self.__yql._construct()
        url = _yahoo_api+"?"+ urlencode(dict(q=url, format="json"))
        response = super(_Api_Request, self).get(url)
        return _Api_Response(response)

    def xml(self):
        url = self.__yql._construct()
        url = _yahoo_api+"?"+ urlencode(dict(q=url, format="xml"))
        response = super(_Api_Request, self).get(url)
        return _Api_Response(response)
