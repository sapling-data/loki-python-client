#
# Copyright (c) 2024 All Rights Reserved, Sapling Data Inc., https://saplingdata.com
#
# Licensed under the MIT License (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is in the "LISENSE" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

__author__ = 'ada'

import unittest
import loki.utils


class TestUrnToUrl(unittest.TestCase):

    known_vals = {None:                                     None,
                  'urn:com:lokipy:test:abc':                'urn/com/lokipy/test/abc'
                  }

    def test_urn_to_url(self):
        for val in self.known_vals:
            result = loki.utils.urn_to_url(val)
            self.assertEqual(result, self.known_vals[val])


class TestToNumber(unittest.TestCase):
    """ Unit tests to evaluate the behavior of to_number. """

    known_vals = {'':                                       None,
                  'Not Applicable':                         None,
                  'per person not applicable':              None,
                  'There is no decimal value.':             None,
                  '$0':                                     '0',
                  '$6850':                                  '6850',
                  '6,850':                                  '6850',
                  '6,850,000':                              '6850000',
                  '$6,850':                                 '6850',
                  '$6850 per person | $13700 per group':    '13700'}

    def test_to_number(self):
        """ Tests that to_number returns known decimal-formatted values given various input. """
        for val in self.known_vals:
            result = loki.utils.to_number(val)
            self.assertEqual(result, self.known_vals[val])


class TestToLokiDate(unittest.TestCase):
    """ Unit tests to evaluate the behavior of to_loki_date. """

    known_vals = {'':                       '0000-00-00',
                  '1/1/16':                 '2016-01-01',
                  '01/01/2016':             '2016-01-01'}

    def test_to_loki_date(self):
        """ Tests that to_loki_date returns loki-formatted date values given various input. """
        for val in self.known_vals:
            result = loki.utils.to_loki_date(val)
            self.assertEqual(result, self.known_vals[val])


class TestToNone(unittest.TestCase):
    """ Unit tests to evaluate the behavior of to_none. """

    known_vals = {'':                       None,
                  'Not an empty field.':    'Not an empty field.'}

    def test_to_loki_date(self):
        """ Tests that to_none returns a value of None given various input. """
        for val in self.known_vals:
            result = loki.utils.to_none(val)
            self.assertEqual(result, self.known_vals[val])
        result = loki.utils.to_none([])
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
