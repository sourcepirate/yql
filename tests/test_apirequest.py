
import unittest

from yql.api._api_request import _Api_Request

class TestApiRequest(unittest.TestCase):


    def test_request(self):

        api_request = _Api_Request(table="html")
        api_request.add_filter("url", "http://en.wikipedia.org/wiki/Yahoo")
        response = api_request.json()
        self.assertEqual(response.result.query.count, 1)
