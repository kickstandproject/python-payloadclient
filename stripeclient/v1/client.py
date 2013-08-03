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
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warlock

from stripeclient.common import http
from stripeclient.v1 import queues
from stripeclient.v1 import schemas


class Client(object):

    def __init__(self, *args):
        self.http_client = http.HTTPClient(*args)
        self.schemas = schemas.Controller(self.http_client)
        self.queues = queues.Controller(
            self.http_client, self._get_model('queue')
        )

    def _get_model(self, name):
        schema = self.schemas.get(name)
        return warlock.model_factory(schema.raw())
