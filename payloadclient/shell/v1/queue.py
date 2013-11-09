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


class CreateQueue(base.CreateCommand):
    """Create a queue."""

    log = logging.getLogger(__name__ + '.CreateQueue')
    resource = 'queues'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', help='The name of the queue.')
        parser.add_argument(
            '--description', help='A short description of the queue.')
        parser.add_argument(
            '--disabled', type=bool, default=False, help='(Default: False)')

    def args2body(self, parsed_args):
        body = {
            'disabled': parsed_args.disabled,
            'name': parsed_args.name,
        }
        if parsed_args.description:
            body['description'] = parsed_args.description

        return body


class DeleteQueue(base.DeleteCommand):
    """Delete a given queue."""

    log = logging.getLogger(__name__ + '.DeleteQueue')
    resource = 'queues'


class ListQueue(base.ListCommand):
    """List queues."""

    list_columns = [
        'uuid',
        'name',
        'description',
        'disabled',
        'user_id',
        'project_id',
        'created_at',
        'updated_at',
    ]
    log = logging.getLogger(__name__ + '.ListQueue')
    resource = 'queues'


class ShowQueue(base.ShowCommand):
    """Show information of a given queue."""

    log = logging.getLogger(__name__ + '.ShowQueue')
    resource = 'queues'
