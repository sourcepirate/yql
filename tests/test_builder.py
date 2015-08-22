
import unittest

from yql._builder import  _Filter
from yql._builder import  _YQLBuilder


class TestBuilder(unittest.TestCase):

    def test_filter(self):
        '''
          Testing the Filter interface where it
          is yield the proper string
        '''

        _filter = _Filter('name', "sathya")
        self.assertEqual(_filter.el, "name = sathya")

    def test_builder(self):

        _yql = _YQLBuilder("user")

        _yql.filter("name", "sathya")

        actual = "SELECT * FROM user WHERE name = sathya"

        self.assertEqual(_yql.el, actual)
