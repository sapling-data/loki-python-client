#
# Copyright (c) 2024 All Rights Reserved, Sapling Data Inc., https://saplingdata.com
#
# Licensed under the MIT License (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is in the "LISENSE" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

__author__ = 'mtruchard'

import unittest
from loki import Loki


class TestUrnToUrl(unittest.TestCase):

    known_vals = {
                  'urn:com:lokipy:test:abc':                'urn/com/lokipy/test/abc'
                  }

    def test_urn_to_url_path(self):
        loki = Loki()
        for val in self.known_vals:
            result = loki.web.urn_to_url_path(val)
            self.assertEqual(result, self.known_vals[val])

if __name__ == "__main__":
    unittest.main()
