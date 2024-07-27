#
# Copyright (c) 2024 All Rights Reserved, Sapling Data Inc, https://saplingdata.com
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


class Data:
    def __init__(self, loki):
        self.loki = loki

    def list(self, urn, /, *, output_view = None, data_space_urn = None):
        urlParams = { "format":"json", "outputView":output_view, "dataSpaceUrn": data_space_urn }
        url = self.loki.web.web_service_url('urn:com:loki:core:model:webServices:list', subject_urn = urn, urlParams = urlParams)
        r = requests.get(url, auth=(self.loki._username, self.loki._password))
        return ListResults(r)

    def save_entity(self, data, entity_view_urn, /, *, data_space_urn = None):
        urlParams = { "format":"json", "dataSpaceUrn": data_space_urn }
        url = self.loki.web.web_service_url(entity_view_urn, subject_urn = data.urn, urlParams = urlParams)
        r = requests.post(url, data=json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                          auth=(self.loki._username, self.loki._password))
        return SaveResponse(r)

    def load_entity(self, urn, entity_view_urn, /, *, data_space_urn = None):
        urlParams = { "format":"json", "dataSpaceUrn": data_space_urn }
        url = self.loki.web.web_service_url(entity_view_urn, subject_urn = urn, urlParams = urlParams)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        return LoadEntityResponse(r)

    def load_resource(self, urn, /, *, data_space_urn = None):
        urlParams = { "format":"json", "dataSpaceUrn": data_space_urn }
        url = self.loki.web.web_service_url("urn:com:loki:core:model:webServices:resource", subject_urn = urn, urlParams = urlParams)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        return LoadResourceResponse(r)

    def download_resource(self, urn, file_name, /, *, data_space_urn = None):
        urlParams = { "format":"json", "dataSpaceUrn": data_space_urn }
        file_name = os.path.expanduser(file_name)
        url = self.loki.web.web_service_url("urn:com:loki:core:model:webServices:resource", subject_urn = urn, urlParams = urlParams)
        r = requests.get(url, headers={'Content-type': 'application/json', 'Accept': 'application/json'},
                         auth=(self.loki._username, self.loki._password))
        with open(file_name, 'wb') as f:
            f.write(r.content)
        return LoadResourceResponse(r)

    def query(self, /, *, query_urn = None, query = None, data_space_urn = None):
        urlParams = {
            "format":"json",
            "dataSpaceUrn": data_space_urn
        }
        if query_urn is not None:
            urlParams["queryUrn"] = query_urn
        elif query is not None:
            urlParams["query"] = query
        else:
             raise Exception("Loki query requres either a query_urn or a query")
        url = self.loki.web.web_service_url("urn:com:loki:core:model:webServices:query", urlParams = urlParams)
        data = {"queryUrn": query_urn}
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
