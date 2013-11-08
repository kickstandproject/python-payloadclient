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

import logging

from payloadclient.shell.v1 import base


class CreateAgent(base.CreateCommand):
    """Create an agent."""

    log = logging.getLogger(__name__ + '.CreateAgent')
    resource = 'agents'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', help='The name of the agent.')

    def args2body(self, parsed_args):
        body = {
            'name': parsed_args.name,
        }

        return body


class DeleteAgent(base.DeleteCommand):
    """Delete a given agent."""

    log = logging.getLogger(__name__ + '.DeleteAgent')
    resource = 'agents'


class ListAgent(base.ListCommand):
    """List agents."""

    list_columns = [
        'uuid',
        'user_id',
        'created_at',
        'updated_at',
    ]
    log = logging.getLogger(__name__ + '.ListAgent')
    resource = 'agents'


class ShowAgent(base.ShowCommand):
    """Show information of a given agent."""

    log = logging.getLogger(__name__ + '.ShowAgent')
    resource = 'agents'
