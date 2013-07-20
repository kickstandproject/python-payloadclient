# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (C) 2013 PolyBeacon, Inc.
#
# Author: Paul Belanger <paul.belanger@polybeacon.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warlock

from stripeclient import test
from stripeclient.tests import utils
from stripeclient.v1 import queues


FIXTURES = {
    '/v1/queues/1': {
        'DELETE': (
            {},
            {
                'id': '1',
            },
        ),
        'GET': (
            {},
            {
                'id': '1',
                'name': 'support',
            },
        ),
        'PUT': (
            {},
            {
                'id': '1',
                'name': 'sales',
            },
        ),
    },
    '/v1/queues': {
        'GET': (
            {},
            [
                {
                    'id': '1',
                    'name': 'support',
                },
                {
                    'id': '2',
                    'name': 'sales',
                },
            ],
        ),
        'POST': (
            {},
            {
                'id': '1',
                'name': 'support',
            },
        ),
    },
}

FAKE_SCHEMA = {
    'name': 'queues',
    'properties': {
        'id': {},
        'name': {}
    }
}

FAKE_MODEL = warlock.model_factory(FAKE_SCHEMA)


class TestCase(test.TestCase):

    def setUp(self):
        super(TestCase, self).setUp()
        self.api = utils.FakeAPI(FIXTURES)
        self.controller = queues.Controller(self.api, FAKE_MODEL)

    def test_create_queue(self):
        json = {
            'id': '1',
            'name': 'support',
        }
        queue = self.controller.create(json)
        self.assertEqual(queue.id, '1')
        self.assertEqual(queue.name, 'support')

    def test_delete_queue(self):
        self.controller.delete('1')
        expect = [(
            'DELETE', '/v1/queues/1', {}, None
        )]
        self.assertEqual(self.api.calls, expect)

    def test_edit_queue(self):
        json = {
            'name': 'sales',
        }
        queue = self.controller.edit('1', json)
        self.assertEqual(queue.id, '1')
        self.assertEqual(queue.name, 'sales')

    def test_get_one_queue(self):
        queue = self.controller.get_one('1')
        self.assertEqual(queue.id, '1')
        self.assertEqual(queue.name, 'support')

    def test_get_all_queue(self):
        queues = list(self.controller.get_all())
        self.assertEqual(queues[0].id, '1')
        self.assertEqual(queues[0].name, 'support')
        self.assertEqual(queues[1].id, '2')
        self.assertEqual(queues[1].name, 'sales')
