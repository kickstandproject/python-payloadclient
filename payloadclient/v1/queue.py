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
    'description',
    'disabled',
    'name',
]

UPDATE_ATTRIBUTES = [
    'description',
    'disabled',
    'name',
]


class Queue(base.Resource):
    def __repr__(self):
        return '<Queue %s>' % self._info


class QueueManager(base.Manager):

    resource_class = Queue

    def __check_keys(self, attributes, **kwargs):
        keys = {}
        for (key, value) in kwargs.items():
            if key in attributes:
                keys[key] = value
            else:
                raise exception.InvalidAttribute()

        return keys

    def __create(self, attributes, path, **kwargs):
        keys = self.__check_keys(attributes=attributes, **kwargs)

        return self._create(path, keys)

    def __update(self, attributes, path, **kwargs):
        keys = self.__check_keys(attributes=attributes, **kwargs)

        return self._update(path, keys)

    @staticmethod
    def _path(uuid=None):
        return '/v1/queues/%s' % uuid if uuid else '/v1/queues'

    def add_member(self, uuid, agent_uuid):
        path = '%s/%s/%s' % (self._path(uuid=uuid), 'members', agent_uuid)

        return self.__create(
            attributes=None, path=path)

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

    def list_member(self, uuid):
        path = '%s/%s' % (self._path(uuid=uuid), 'members')

        return self._list(path)

    def remove_member(self, uuid, agent_uuid):
        path = '%s/%s/%s' % (self._path(uuid=uuid), 'members', agent_uuid)

        return self._delete(path)

    def update(self, uuid, **kwargs):
        path = self._path(uuid=uuid)

        return self.__update(
            attributes=UPDATE_ATTRIBUTES, path=path, **kwargs)
