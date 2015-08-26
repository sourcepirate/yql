from ._api_request import _Api_Request

class YRequest(object):

    def __init__(self, *args, **kwargs):

        self._api_request = _Api_request(*args, **kwargs)
        # super(YRequest, self).__init__(*args, **kwargs)

    def get(self):
        pass

    def update_filter(self, *args, **kwargs):
        pass
