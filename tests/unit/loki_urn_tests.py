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


class TestToLokiUrnSegment(unittest.TestCase):
    """ Unit tests to evaluate the behavior of to_loki_urn_segment. """

    known_vals = {'':                       None,
                  'Clair':                  'Clair',
                  'St. Clair':              'St.Clair',
                  'MI - St. Clair':         'MI-St.Clair',
                  'MI - St. Clair!':        'MI-St.Clair'}

    def testGetValidSegment(self):
        """ Tests that to_loki_urn_segment returns a value of None given various input. """
        loki = Loki("config.txt")
        for val in self.known_vals:
            result = loki.urn.get_valid_segment(val)
            self.assertEqual(self.known_vals[val], result)
            
    def testIsNew(self):
        loki = Loki("config.txt")
        self.assertEqual(loki.urn.is_new('urn:com:loki:$'),True)
        self.assertEqual(loki.urn.is_new('urn:$:loki:data!text.txt'),True)
        self.assertEqual(loki.urn.is_new('urn:com:loki:8181'),False)
        
    def testGetLastSegment(self):
        loki = Loki("config.txt")
        self.assertEqual(loki.urn.get_last_segment('urn:com:loki!test.jpg'),'test.jpg')
        self.assertEqual(loki.urn.get_last_segment('urn#embeded1'),'embeded1')
        self.assertEqual(loki.urn.get_last_segment('urn:$:data:test2'),'test2')
        self.assertEqual(loki.urn.get_last_segment(''),'')
        self.assertEqual(loki.urn.get_last_segment(None),None)


if __name__ == "__main__":
    unittest.main()
