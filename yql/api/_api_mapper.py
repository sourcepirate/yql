
import json

from datetime import datetime

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

    def __init__(self, json_obj , *args, **kwargs):

        d = json.loads(json_obj)
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [ObjectMapper(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, ObjectMapper(b) if isinstance(b, dict) else b)
