
import json

from datetime import datetime
import six

class _object_decoder(json.JSONDecoder):

    '''A helper class to decode datetime
       objects a well

    '''

    def __init__(self, *args, **kwargs):

        super(_object_decoder, self).__init__(object_hook= self._mapper)


    def _mapper(self, obj):

        if '__class__' in obj:

            class_name = obj.pop('__class__')
            module_name = obj.pop('__module__')
            module = __import__(module_name)

            _class = getattr(module, class_name)

            if _class is datetime:
                return str(obj)
            else:
                return obj

class ObjectMapper(object):

    '''Converts a given dict to object

    Args:
       json_obj(dict): The dict which has to be mapped like an object


    Example:

       >>> obj = ObjectMapper(dict_obj)
       >>> dir(obj)

    '''

    def __init__(self, json_obj , *args, **kwargs):

        d = json_obj
        for a, b in six.iteritems(d):
            if isinstance(b, (list, tuple)):
               setattr(self, a, [ObjectMapper(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, ObjectMapper(b) if isinstance(b, dict) else b)

    @staticmethod
    def to_object(json_dict, *args, **kwargs):
        '''Object Method converts the dict to object

        Args:

           json_dict(dict): The dict that has to be converted into object

        Returns:

           ObjectMapper: Returns the ObjectMapper instance.

        '''
        return ObjectMapper(json_dict, *args, **kwargs)
