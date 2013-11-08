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


class Base(object):

    url = '/v1'

    def __init__(self, http_client, model):
        self.http_client = http_client
        self.model = model

    def create(self, body):
        """Create an object."""
        url = self.url
        resp, body = self.http_client.json_request('POST', url, body=body)

        return self.model(body)

    def delete(self, uuid):
        """Delete an object."""
        url = '%s/%s' % (self.url, uuid)
        self.http_client.json_request('DELETE', url)

    def edit(self, uuid, body):
        """Edit an object."""
        url = '%s/%s' % (self.url, uuid)
        resp, body = self.http_client.json_request('PUT', url, body=body)

        return self.model(body)

    def get_all(self):
        """List all objects."""
        url = self.url
        resp, body = self.http_client.json_request('GET', url)

        for item in body:
            yield self.model(item)

    def get_one(self, uuid):
        """Get a single object."""
        url = '%s/%s' % (self.url, uuid)
        resp, body = self.http_client.json_request('GET', url)
        body.pop('self', None)

        return self.model(**body)
