# Copyright (c) 2015

#  author: plasmashadow.
#  company: StrawHatPirates.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software


#base url for yahoo query library.

from .api._api_request import _Api_Request
from .api._api_response import _Api_Response

from .api._api_mapper import ObjectMapper

YRequest = _Api_Request
YResponse = _Api_Response

__all__= ['YRequest', 'YResponse', 'ObjectMapper']
