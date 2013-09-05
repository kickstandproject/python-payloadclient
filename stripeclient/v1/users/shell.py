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

from cliff import command
from cliff import lister
from cliff import show

from stripeclient.openstack.common import log as logging

LOG = logging.getLogger(__name__)


class Add(show.ShowOne):

    def get_parser(self, prog_name):
        parser = super(Add, self).get_parser(prog_name)
        parser.add_argument('name', metavar='name', help='User name')
        parser.add_argument(
            'password', metavar='password', help='User password'
        )
        parser.add_argument(
            '--id', type=int, default=None,
            help='(Default: None)'
        )
        parser.add_argument(
            '--email', type=str, default=None,
            help='(Default: None)'
        )

        return parser

    def take_action(self, parsed_args):

        json = {
            'id': parsed_args.id,
            'email': parsed_args.email,
            'name': parsed_args.name,
            'password': parsed_args.password,
        }

        res = self.app.http_client.users.create(json)

        return zip(*sorted(res.items()))


class Delete(command.Command):

    def get_parser(self, prog_name):
        parser = super(Delete, self).get_parser(prog_name)
        parser.add_argument('id', metavar='id', help='User ID')

        return parser

    def take_action(self, parsed_args):
        self.app.http_client.users.delete(parsed_args.id)


class Show(lister.Lister):

    def get_parser(self, prog_name):
        parser = super(Show, self).get_parser(prog_name)
        parser.add_argument(
            'id', type=int, nargs='?', default=None,
            help='(Default: None)'
        )

        return parser

    def take_action(self, parsed_args):
        if parsed_args.id:
            data = [self.app.http_client.users.get_one(parsed_args.id)]
        else:
            data = self.app.http_client.users.get_all()

        columns = (
            'id',
            'email',
            'name',
            'password',
            'created_at',
            'updated_at',
        )

        res = ((
            q.id,
            q.email,
            q.name,
            q.password,
            q.created_at,
            q.updated_at,
        ) for q in data)

        return (columns, res)
