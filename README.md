##YQL
[![Build Status](https://travis-ci.org/plasmashadow/yql.svg?branch=master)](https://travis-ci.org/plasmashadow/yql)
[![PyPI version](https://badge.fury.io/py/yql.svg)](http://badge.fury.io/py/yql)

##Description:
YQL is a thin wrapper for Yahoo Query Language.

##Installation:

```python
   pip install yql

```

##Usage

Inorder to create a yahoo request you can use a YRequest call from YQL.

```python
from yql import YRequest
import logging

log = logging.getLogger(__name__)

y = YRequest(table="html")
y.add_filter("url", "http://en.wikipedia.org/wiki/Yahoo")
response = y.json()
log.info(response)

```
Since yql comes with the Object mapper you can directly reference the
sub keys of a json.

```python

log.info(response.query.count)

```

##LICENSE
MIT
