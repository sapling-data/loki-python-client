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

import unittest
from loki import Loki

config_file = "~/loki-python-client/config.txt"


class TestList(unittest.TestCase):
    """ Unit tests to evaluate the behavior of loki.data(). """

    def test_list(self):
        loki = Loki(config_file)

        urn = "urn:com:loki:core:model:types"
        
        result = loki.data.list(urn,None)
        print(result)
        self.assertEqual(200, result.status_code)
        types = result.json()["results"]
        for t in types:
            print(t["urn"])
        
    def test_load_entity(self):
        loki = Loki(config_file)

        urn = "urn:com:loki:meta:model:types:error"
        view = "urn:com:loki:meta:model:types:entityView"
        
        result = loki.data.load_entity(urn,view,None)
        self.assertEqual(200, result.status_code)
        print(result)
        print(result.json())

    def test_load_resource(self):
        loki = Loki(config_file)

        urn = "urn:com:loki:core:model:api:list!listApi.html"

        result = loki.data.load_resource(urn,None)
        self.assertEqual(200, result.status_code)
        print(result)
        print(result.content)

    def test_download_resource(self):
        loki = Loki(config_file)

        urn = "urn:com:loki:core:model:api:list!listApi.html"

        result = loki.data.download_resource(urn,None,"~/listApi.html")
        self.assertEqual(200, result.status_code)
        print(result)
        print(result.content)

    def test_query(self):
        loki = Loki(config_file)

        query_urn = "urn:com:loki:examples:model:queries:listDocuments"

        result = loki.data.query(query_urn,None)
        print(result.get_response())
        print(result.get_response().content)
        print(result.get_response().json())
        self.assertEqual(200, result.get_response().status_code)
        for r in result.to_array():
            for v in r:
                print(v)


if __name__ == "__main__":
    unittest.main()
