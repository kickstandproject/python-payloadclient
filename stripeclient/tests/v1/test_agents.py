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
from stripeclient.v1 import agents


FIXTURES = {
    '/v1/agents/1': {
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
                'name': 'Paul Belanger',
            },
        ),
        'PUT': (
            {},
            {
                'id': '1',
                'name': 'Paul Belanger',
            },
        ),
    },
    '/v1/agents': {
        'GET': (
            {},
            [
                {
                    'id': '1',
                    'name': 'Paul Belanger',
                },
                {
                    'id': '2',
                    'name': 'Leif Madsen',
                },
            ],
        ),
        'POST': (
            {},
            {
                'id': '1',
                'name': 'Paul Belanger',
            },
        ),
    },
}

FAKE_SCHEMA = {
    'name': 'agents',
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
        self.controller = agents.Controller(self.api, FAKE_MODEL)

    def test_create_agent(self):
        json = {
            'id': '1',
            'name': 'Paul Belanger',
        }
        res = self.controller.create(json)
        self.assertEqual(res.id, '1')
        self.assertEqual(res.name, 'Paul Belanger')

    def test_delete_agent(self):
        self.controller.delete('1')
        expect = [(
            'DELETE', '/v1/agents/1', {}, None
        )]
        self.assertEqual(self.api.calls, expect)

    def test_edit_agent(self):
        json = {
            'name': 'Paul Belanger',
        }
        res = self.controller.edit('1', json)
        self.assertEqual(res.id, '1')
        self.assertEqual(res.name, 'Paul Belanger')

    def test_get_one_agent(self):
        res = self.controller.get_one('1')
        self.assertEqual(res.id, '1')
        self.assertEqual(res.name, 'Paul Belanger')

    def test_get_all_agent(self):
        res = list(self.controller.get_all())
        self.assertEqual(res[0].id, '1')
        self.assertEqual(res[0].name, 'Paul Belanger')
        self.assertEqual(res[1].id, '2')
        self.assertEqual(res[1].name, 'Leif Madsen')
