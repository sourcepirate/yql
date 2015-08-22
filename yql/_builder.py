
import string
import six

class safelist(list):

    def get(self, index, default=None):
        '''Safe get for list like dictionary

        Args:
           index(int): The index of the element in the list
           default(object): default object to return if the element
           is not present int the list

        Returns:
           object: Object from the list

        '''
        try:
            return self.__getitem__(index)
        except IndexError:
            return default


class _Filter(object):

    '''Filter the match of particular key to a value
       >>>_filter = _Filter('key', 'value')
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
        ''' Returns the String expression for a Filter
        >>>_filter = _Filter('key', 'value')
        >>>_filter.el
        key = value
        >>>
        '''
        return str(self)




class _YQLBuilder(object):

    '''YQL query Builder

      Args:
         table(str): name of the table
    '''

    def __init__(self, table):

        self.table = table
        self._filters = []

    def filter(self, name, value):

        '''Adds a new condtion to YQL

        Args:
           name(str): name of the column
           value(str,int, float): value to which the column has be
                                  matched.

        Returns:
           _YQLBuilder: return the current instance of the object
                        for chaining.

        '''

        self._filters.append(_Filter(name, value))
        return self

    def _construct(self):

        '''Method to construct the Query String

        Returns:
           str: expression for query.
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
        '''Getter for expression language.

        Returns:
           str: query expression.
        '''

        return self._construct()
