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

import testtools

from payloadclient.tests import utils
from payloadclient.v1 import queue

QUEUE = {
    'created_at': '2013-11-08T20:14:01.921966',
    'description': 'Sales',
    'disabled': False,
    'name': 'sales',
    'updated_at': None,
    'user_id': 'dbeead071b6e4f168f00c702888b6de9',
    'uuid': 'b5142338-d88a-403e-bb14-e1fba0a318d2',
}

CREATE_QUEUE = {
    'description': '24/7 customer support.',
    'disabled': False,
    'name': 'suppoert',
}

UPDATE_QUEUE = {
    'description': 'Sales support.',
    'disabled': True,
    'name': 'sales',
}

FIXTURES = {
    '/v1/queues': {
        'GET': (
            {},
            [QUEUE],
        ),
        'POST': (
            {},
            QUEUE,
        ),
    },
    '/v1/queues/%s' % QUEUE['uuid']: {
        'GET': (
            {},
            QUEUE,
        ),
        'DELETE': (
            {},
            None,
        ),
        'PUT': (
            {},
            UPDATE_QUEUE,
        ),
    },
}


class QueueManagerTest(testtools.TestCase):

    def setUp(self):
        super(QueueManagerTest, self).setUp()
        self.api = utils.FakeAPI(FIXTURES)
        self.manager = queue.QueueManager(self.api)

    def test_create(self):
        res = self.manager.create(**CREATE_QUEUE)
        expect = [
            ('POST', '/v1/queues', {}, CREATE_QUEUE),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertTrue(res)

    def test_delete(self):
        res = self.manager.delete(uuid=QUEUE['uuid'])
        expect = [
            ('DELETE', '/v1/queues/%s' % QUEUE['uuid'], {}, None),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(res, None)

    def test_list(self):
        res = self.manager.list()
        expect = [
            ('GET', '/v1/queues', {}, None),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(len(res), 1)

    def test_show(self):
        res = self.manager.get(uuid=QUEUE['uuid'])
        expect = [
            ('GET', '/v1/queues/%s' % QUEUE['uuid'], {}, None),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertEqual(res.uuid, QUEUE['uuid'])

    def test_update(self):
        res = self.manager.update(uuid=QUEUE['uuid'], **UPDATE_QUEUE)
        expect = [
            ('PUT', '/v1/queues/%s' % QUEUE['uuid'], {}, UPDATE_QUEUE),
        ]
        self.assertEqual(self.api.calls, expect)
        self.assertTrue(res)
