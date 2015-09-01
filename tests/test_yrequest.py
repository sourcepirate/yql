import unittest

from yql.api import YRequest

class  TestYRequest(unittest.TestCase):

    def test_get_json(self):

        ''' Testing Default Expression without a table name
            Default Expression is 'Show Tables'
        '''
        y_request = YRequest()
        response = y_request.get(format="json", expression="show tables")
        self.assertEqual(response.result.query.count, 134)

    def test_get_xml(self):

        ''' Testing Default Expression without a table name
            Default Expression is 'Show Tables'
        '''
        y_request = YRequest()
        response = y_request.get(format="xml", expression="show tables")
        self.assertEqual(response.status, 200)

    def test_list_tables(self):

        ''' Testing List tables to list display all tables

            Default expression is 'show tables'
        '''

        resposne = YRequest.list_tables(format="json")
        self.assertEqual(resposne.status, 200)
        
