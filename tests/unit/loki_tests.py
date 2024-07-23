#
# Copyright (c) 2024 All Rights Reserved, SaplingData Inc., https://saplingdata.com
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


class TestLokiClient(unittest.TestCase):
    def testReadConfig(self):
        loki = Loki("./tests/unit/config.txt")
        self.assertEqual(loki._username, "testuser")
        self.assertEqual(loki._password, "testpassword")
        self.assertEqual(loki._hosturl, "https://apiurl")

    def testPassConfig(self):
        loki = Loki(username='test2user', password='test2password', hosturl="https://testurl")
        self.assertEqual(loki._username, "test2user")
        self.assertEqual(loki._password, "test2password")
        self.assertEqual(loki._hosturl, "https://testurl")
