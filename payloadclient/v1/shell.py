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

from payloadclient.openstack.common import log as logging

LOG = logging.getLogger(__name__)


class AgentAdd(show.ShowOne):

    def get_parser(self, prog_name):
        parser = super(AgentAdd, self).get_parser(prog_name)
        parser.add_argument(
            'user_id', metavar='user_id', help='User ID'
        )

        return parser

    def take_action(self, parsed_args):
        json = {
            'user_id': parsed_args.user_id,
        }

        res = self.app.http_client.agents.create(json)

        return zip(*sorted(res.items()))


class AgentDelete(command.Command):

    def get_parser(self, prog_name):
        parser = super(AgentDelete, self).get_parser(prog_name)
        parser.add_argument('uuid', metavar='uuid', help='Agent UUID')

        return parser

    def take_action(self, parsed_args):
        self.app.http_client.agents.delete(uuid=parsed_args.uuid)


class AgentShow(lister.Lister):

    def get_parser(self, prog_name):
        parser = super(AgentShow, self).get_parser(prog_name)
        parser.add_argument(
            'uuid', nargs='?', default=None,
            help='(Default: None)'
        )

        return parser

    def take_action(self, parsed_args):
        if parsed_args.uuid:
            data = [self.app.http_client.agents.get_one(uuid=parsed_args.uuid)]
        else:
            data = self.app.http_client.agents.get_all()

        columns = (
            'uuid',
            'user_id',
            'created_at',
            'updated_at',
        )

        res = ((
            q.uuid,
            q.user_id,
            q.created_at,
            q.updated_at,
        ) for q in data)

        return (columns, res)


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

        return parser

    def take_action(self, parsed_args):
        json = {
            'description': parsed_args.description,
            'disabled': parsed_args.disabled,
            'name': parsed_args.name,
        }

        data = self.app.http_client.queues.create(json)

        return zip(*sorted(data.items()))


class QueueDelete(command.Command):

    def get_parser(self, prog_name):
        parser = super(QueueDelete, self).get_parser(prog_name)
        parser.add_argument('uuid', metavar='uuid', help='Queue UUID')

        return parser

    def take_action(self, parsed_args):
        self.app.http_client.queues.delete(uuid=parsed_args.uuid)


class QueueShow(lister.Lister):

    def get_parser(self, prog_name):
        parser = super(QueueShow, self).get_parser(prog_name)
        parser.add_argument(
            'uuid', nargs='?', default=None,
            help='(Default: None)'
        )

        return parser

    def take_action(self, parsed_args):
        if parsed_args.uuid:
            data = [self.app.http_client.queues.get_one(uuid=parsed_args.uuid)]
        else:
            data = self.app.http_client.queues.get_all()

        columns = (
            'uuid',
            'description',
            'disabled',
            'name',
            'user_id',
            'created_at',
            'updated_at',
        )

        res = ((
            q.uuid,
            q.description,
            q.disabled,
            q.name,
            q.user_id,
            q.created_at,
            q.updated_at,
        ) for q in data)

        return (columns, res)
