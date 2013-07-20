# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC.
# Copyright (C) 2013 PolyBeacon, Inc.
# All Rights Reserved.
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
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.

from stripeclient.common import utils


@utils.arg('id', metavar='<QUEUE_ID>', help='ID of queue to create.')
@utils.arg('name', metavar='<NAME>', help='Name.')
def do_create_queue(gc, args):
    json = {
        'id': args.id,
        'name': args.name,
    }
    queue = gc.queues.create(json)
    utils.print_dict(queue)


@utils.arg('id', metavar='<QUEUE_ID>', help='ID of queue to delete.')
def do_delete_queue(gc, args):
    gc.queues.delete(args.id)


@utils.arg('id', metavar='<QUEUE_ID>', help='ID of queue to edit.')
@utils.arg('name', metavar='<NAME>', help='Name.')
def do_edit_queue(gc, args):
    json = {
        'name': args.name,
    }
    queue = gc.queues.edit(args.id, json)
    utils.print_dict(queue)


@utils.arg('id', metavar='<QUEUE_ID>', help='ID of queue to describe.')
def do_show_queue(gc, args):
    """Describe a specific queue."""
    queue = gc.queues.get_one(args.id)
    utils.print_dict(queue)


def do_show_queues(gc, args):
    queues = gc.queues.get_all()
    columns = ['ID', 'Name']
    utils.print_list(queues, columns)
