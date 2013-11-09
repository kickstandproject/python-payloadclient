# -*- coding: utf-8 -*-
# Copyright (c) 2013 PolyBeacon, Inc.

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from payloadclient.common import base
from payloadclient.common import exception

CREATE_ATTRIBUTES = [
    'uuid',
]


class Agent(base.Resource):
    def __repr__(self):
        return '<Agent %s>' % self._info


class AgentManager(base.Manager):

    resource_class = Agent

    def __create(self, attributes, path, **kwargs):
        keys = {}
        for (key, value) in kwargs.items():
            if key in attributes:
                keys[key] = value
            else:
                raise exception.InvalidAttribute()

        return self._create(path, keys)

    @staticmethod
    def _path(uuid=None):
        return '/v1/agents/%s' % uuid if uuid else '/v1/agents'

    def create(self, **kwargs):
        path = self._path()

        return self.__create(
            attributes=CREATE_ATTRIBUTES, path=path, **kwargs)

    def delete(self, uuid):
        return self._delete(self._path(uuid=uuid))

    def get(self, uuid):
        try:
            return self._list(self._path(uuid=uuid))[0]
        except IndexError:
            return None

    def list(self):
        return self._list(self._path())
