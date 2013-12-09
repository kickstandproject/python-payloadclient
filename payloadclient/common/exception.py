# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC.
# Copyright (C) 2013 PolyBeacon, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys


_code_map = {}
for obj_name in dir(sys.modules[__name__]):
    if obj_name.startswith('HTTP'):
        obj = getattr(sys.modules[__name__], obj_name)
        _code_map[obj.code] = obj


def from_response(response, error=None):
    """Return an instance of an HTTPException based on httplib response."""
    cls = _code_map.get(response.status, HTTPException)

    return cls(error)


class BaseException(Exception):
    """An error occurred."""
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message or self.__class__.__doc__


class CommandError(BaseException):
    """Invalid usage of CLI."""


class CommunicationError(BaseException):
    """Unable to communicate with server."""


class InvalidAttribute(BaseException):
    pass


class InvalidEndpoint(BaseException):
    pass


class HTTPException(Exception):
    """Base exception for all HTTP-derived exceptions."""
    code = 'N/A'

    def __init__(self, details=None):
        self.details = details or self.__class__.__name__

    def __str__(self):
        return "%s (HTTP %s)" % (self.details, self.code)
