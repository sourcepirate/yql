
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

    def __init__(self, name, value, type="unicode"):

        '''Represents the Filter in yql query
         For example: select * from query where age = 26 (is integer)
                      select * from query where name = 'sathya' (unicode)
                      select * from query where quote = "As long as i do i will continue to do"

        Args:
            name(str):              Name of the key.
            value(str, int ,float): Value to be use for query.
            type:                   Represents the type of data used as a value.
        '''

        self.name = name
        self.operator = "="
        if type == "integer":
            self.value = value
        elif type== "unicode":
            self.value = "'{0}'".format(value)
        elif type== "string":
            self.value = '"{0}"'.format(value)



    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.operator, self.value)

    def __repr__(self):

        return repr("{0} {1} {2}".format(self.name, self.operator, self.value))

    @property
    def el(self):
        ''' Returns the String expression for a Filter
        >>>_filter = _Filter('key', 'value')
        >>>_filter.el
        key = value
        >>>
        '''
        return str(self)


class _object(object):
    pass

class _YQLBuilder(_object):

    '''YQL query Builder

      Args:
         table(str): name of the table
    '''

    __instance = None

    def __new__(cls, *args, **kwargs):

        '''Making it Singleton
           Such that it return only single instance at
           any point of time.
        '''

        if not cls.__instance:
            cls.__instance = super(_YQLBuilder, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


    def __init__(self, table):

        self.table = table
        self._filters = []
        self.column = None

    def filter(self, name, value ,type= "unicode"):

        '''Adds a new condtion to YQL

        Args:
           name(str): name of the column
           value(str,int, float): value to which the column has be
                                  matched.

        Returns:
           _YQLBuilder: return the current instance of the object
                        for chaining.

        '''

        self._filters.append(_Filter(name, value, type=type))
        return self

    def get(self, *args):

        if args:
            self.column = ','.join(args)
        else:
            self.column = None

    def _construct(self):

        '''Method to construct the Query String

        Returns:
           str: expression for query.
        '''

        if not self.column:
            self.column = "*"


        statement = "SELECT {0} FROM {1}".format(self.column, self.table)

        if not self._filters:
            return statement

        statement += " WHERE "

        filters = safelist(self._filters)

        for index, filtor in enumerate(filters):

            statement += filtor.el

            if not filters.get(index+1):
                break

            statement += " and "

        self.column = None

        return statement

    @property
    def el(self):
        '''Getter for expression language.

        Returns:
           str: query expression.
        '''

        return self._construct()
