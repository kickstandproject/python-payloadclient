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
from stripeclient.v1 import client

LOG = logging.getLogger(__name__)


class QueueAdd(show.ShowOne):

    def get_parser(self, prog_name):
        parser = super(QueueAdd, self).get_parser(prog_name)
        parser.add_argument('name', metavar='name', help='Queue name')
        parser.add_argument(
            '--description', type=str, default=None,
            help='(Default: None)'
        )
        parser.add_argument(
            '--disabled', type=bool, default=False,
            help='(Default: False)'
        )
        parser.add_argument(
            '--id', type=int, default=None,
            help='(Default: None)'
        )

        return parser

    def take_action(self, parsed_args):
        endpoint = self.app_args.os_stripe_url
        self.http_client = client.Client(endpoint)
        json = {
            'id': parsed_args.id,
            'description': parsed_args.description,
            'disabled': parsed_args.disabled,
            'name': parsed_args.name,
        }

        data = self.http_client.queues.create(json)

        return zip(*sorted(data.items()))


class QueueDelete(command.Command):

    def get_parser(self, prog_name):
        parser = super(QueueDelete, self).get_parser(prog_name)
        parser.add_argument('id', metavar='id', help='Queue ID')

        return parser

    def take_action(self, parsed_args):
        endpoint = self.app_args.os_stripe_url
        self.http_client = client.Client(endpoint)

        self.http_client.queues.delete(parsed_args.id)


class QueueShow(lister.Lister):

    def get_parser(self, prog_name):
        parser = super(QueueShow, self).get_parser(prog_name)
        parser.add_argument(
            'id', type=int, nargs='?', default=None,
            help='(Default: None)'
        )

        return parser

    def take_action(self, parsed_args):
        endpoint = self.app_args.os_stripe_url
        self.http_client = client.Client(endpoint)

        if parsed_args.id:
            data = [self.http_client.queues.get_one(parsed_args.id)]
        else:
            data = self.http_client.queues.get_all()

        columns = (
            'id',
            'name',
            'description',
            'disabled',
            'created_at',
            'updated_at',
        )

        res = ((
            q.id,
            q.name,
            q.description,
            q.disabled,
            q.created_at,
            q.updated_at,
        ) for q in data)

        return (columns, res)
