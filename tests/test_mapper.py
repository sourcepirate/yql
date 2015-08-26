import unittest

from yql.api._api_mapper import ObjectMapper

class TestMapper(unittest.TestCase):


    def test_mapper(self):


        a = {"a":"b", "c":{"d":"3"}}

        obj = ObjectMapper(a)


        self.assertEqual(obj.c.d,"3")
