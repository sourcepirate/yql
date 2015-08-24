
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
