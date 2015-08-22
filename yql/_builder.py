
import string
import six

class safelist(list):

    def get(self, index, default=None):
        '''
          Safe get for list like dictionary
        '''
        try:
            return self.__getitem__(index)
        except IndexError:
            return default


class _Filter(object):

    '''
      Filter Object for Sql statements
    '''

    def __init__(self, name, value):

        self.name = name
        self.operator = "="
        self.value = value

    def __str__(self):

        return "{} {} {}".format(self.name, self.operator, self.value)

    def __repr__(self):

        return repr("{} {} {}".format(self.name, self.operator, self.value))

    @property
    def el(self):
        return str(self)




class _YQLBuilder(object):

    '''
      Class for building Yql statements.
    '''

    def __init__(self, table):

        self.table = table
        self._filters = []

    def filter(self, name, value):

        '''
          Used for yql with where statements
        '''

        self._filters.append(_Filter(name, value))
        return self

    def _construct(self):

        '''
        Query Constructor for
        Builder Object
        '''

        statement = "SELECT * FROM {}".format(self.table)

        if not self._filters:
            return statement

        statement += " WHERE "

        filters = safelist(self._filters)

        for index, filtor in enumerate(filters):

            statement += filtor.el

            if not filters.get(index+1):
                break

            statement += " and"

        return statement

    @property
    def el(self):

        return self._construct()
