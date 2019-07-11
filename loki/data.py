#
# Copyright (c) 2019 All Rights Reserved, SaplingData LLC, http://saplingdata.com
#
# Licensed under the MIT License (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is in the "LISENSE" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

__author__ = "mtruchard"
__date__ = "$Sep 23, 2015 4:54:32 PM$"

import requests
import os
import json
import utils


class Data:
    def __init__(self, loki):
        self.loki = loki

    def list(self, urn, options):
        """ Issues a get request to Loki via the API using input parameters. """
        url = self.loki._hosturl + '/api/urn/com/loki/core/model/api/list/v/' + utils.urn_to_url(urn)
        params = ""

        if options is not None and options.format is not None :
            params = params + "&format="+options.format;
        else :
            params = params + "&format=json"

        if options is not None and options.outputView  is not None :
            params = params + '&outputView=' + utils.urn_to_url(options.outputView)

        if params != "" :
            url = url + "?" + params[1:]
        r = requests.get(url, auth=(self.loki._username, self.loki._password))
        return r

    def save_entity(self, data, entityViewUrn, options):
        url = self.loki._hosturl \
            + '/api/' + utils.urn_to_url(entityViewUrn) \
            + '/v/' + utils.urn_to_url(data.urn) \
            + '?format=json'
        r = requests.post(url, data=json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                          auth=(self.loki._username, self.loki._password))
        return r

    def load_entity(self, urn, entityViewUrn, options):
        url = self.loki._hosturl \
            + '/api/' + utils.urn_to_url(entityViewUrn) \
            + '/v/' + utils.urn_to_url(urn)
        params = ""

        if options is not None and options.format is not None :
            params = params + "&format="+options.format
        else :
            params = params + "&format=json"

        if params != "" :
            url = url + "?" + params[1:]
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        return r

    def _resource_url(self, urn, options):
        url = self.loki._hosturl \
              + '/api/' + utils.urn_to_url("urn:com:loki:core:model:api:resource") \
              + '/v/' + utils.urn_to_url(urn)
        params = ""

        if options is not None and options.format is not None:
            params = params + "&format=" + options.format
        else:
            params = params + "&format=json"

        if params != "":
            url = url + "?" + params[1:]
        return url

    def load_resource(self, urn, options):
        url = self._resource_url(urn, options)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        return r

    def download_resource(self, urn, options, file_name):
        file_name = os.path.expanduser(file_name)
        url = self._resource_url(urn, options)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        with open(file_name, 'wb') as f:
            f.write(r.content)
        return r