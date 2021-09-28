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
import loki.utils


class Data:
    def __init__(self, loki):
        self.loki = loki

    def list(self, urn, options):
        url = self._web_service_url('urn:com:loki:core:model:api:list', urn, options)
        r = requests.get(url, auth=(self.loki._username, self.loki._password))
        return ListResults(r)

    def save_entity(self, data, entity_view_urn, options):
        url = self._web_service_url(entity_view_urn, data.urn, options)
        r = requests.post(url, data=json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                          auth=(self.loki._username, self.loki._password))
        return SaveResults(r)

    def load_entity(self, urn, entity_view_urn, options):
        url = self._web_service_url(entity_view_urn, urn, options)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        return LoadEntityResponse(r)

    def _resource_url(self, urn, options):
        return self._web_service_url("urn:com:loki:core:model:api:resource", urn, options)

    def _web_service_url(self, service_urn, subject_urn, options):
        url = self.loki._hosturl + '/api/' + loki.utils.urn_to_url(service_urn)
        if subject_urn is not None:
            url = url + '/v/' + loki.utils.urn_to_url(subject_urn)
        params = ""
        if options is not None and options.format is not None:
            params = params + "&format=" + options.format
        else:
            params = params + "&format=json"

        if options is not None and options.outputView  is not None:
            params = params + '&outputView=' + loki.utils.urn_to_url(options.outputView)

        if params != "":
            url = url + "?" + params[1:]
        return url

    def load_resource(self, urn, options):
        url = self._web_service_url("urn:com:loki:core:model:api:resource", urn, options)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        return LoadResourceResponse(r)

    def download_resource(self, urn, options, file_name):
        file_name = os.path.expanduser(file_name)
        url = self._web_service_url("urn:com:loki:core:model:api:resource", urn, options)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        with open(file_name, 'wb') as f:
            f.write(r.content)
        return LoadResourceResponse(r)

    def query(self, query_urn, options):
        url = self._web_service_url("urn:com:loki:core:model:api:query", None, options)
        data = {"queryUrn": query_urn, "mapResults": true}
        r = requests.post(url, data=json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        return QueryResults(r)


class LokiResponse:
    def __init__(self, response, parse):
        self.response = response
        if parse:
            try:
                self.resData = response.json()
            except Exception:
                self.resData = None

    def get_response(self):
        return self.response

    def is_success(self):
        return self.response.status_code == 200

    def get_error(self):
        msg = "Error: "+str(self.response.status_code)
        if self.resData is not None:
            if "errors" in self.resData:
                msg = self.resData["errors"][0].get("systemMessage", msg);
        return msg


class LokiResults(LokiResponse):
    def __init__(self, response):
        LokiResponse.__init__(self, response, True)
        if response.status_code == 200:
            self.results = self.resData["results"]
        else:
            self.results = None

    def __iter__(self):
        self.row = 0
        return self

    def __next__(self):
        if self.results is None:
            raise StopIteration
        if self.row < len(self.results):
            self.row = self.row + 1
            return self.results[self.row-1]
        else:
            raise StopIteration

    def to_array(self):
        a = []
        for v in iter(self):
            a.append(v)
        return a


class SaveResponse(LokiResponse):
    def __init__(self, response):
        LokiResponse.__init__(self, response, True)


class LoadEntityResponse(LokiResponse):
    def __init__(self, response):
        LokiResponse.__init__(self, response, True)

    def get_data(self):
        return self.resData


class LoadResourceResponse(LokiResponse):
    def __init__(self, response):
        parse = (response.status_code != 200)
        LokiResponse.__init__(self, response, parse)

    def get_data(self):
        return self.response.content


class ListResults(LokiResults):
    def __init__(self, response):
        LokiResults.__init__(self, response)


class QueryResults(LokiResults):
    def __init__(self, response):
        LokiResults.__init__(self, response)
