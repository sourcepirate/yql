from ._api_request import _Api_Request
class YRequest(object):

    def __init__(self, *args, **kwargs):

        self._api_request = _Api_Request(*args, **kwargs)
        # super(YRequest, self).__init__(*args, **kwargs)

    def get(self, format=None, expression=None):
        return self._api_request.run(format, expression)

    @classmethod
    def list_tables(cls, format="json"):
        instance = cls()
        return instance.get(format=format, expression="show tables")

    def update_filter(self, *args, **kwargs):
        pass
