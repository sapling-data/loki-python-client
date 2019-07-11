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
        print result
        print result.json()
        
    def test_load_entity(self):
        loki = Loki(config_file)

        urn = "urn:com:loki:meta:model:types:error"
        view = "urn:com:loki:meta:model:types:entityView"
        
        result = loki.data.load_entity(urn,view,None)
        print result
        print result.json()

    def test_load_resource(self):
        loki = Loki(config_file)

        urn = "urn:com:loki:core:model:api:list!listApi.html"

        result = loki.data.load_resource(urn,None)
        print result
        print result.content

    def test_download_resource(self):
        loki = Loki(config_file)

        urn = "urn:com:loki:core:model:api:list!listApi.html"

        result = loki.data.download_resource(urn,None,"~/listApi.html")
        print result
        print result.content


if __name__ == "__main__":
    unittest.main()
