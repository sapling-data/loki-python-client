#
# Copyright (c) 2019 All Rights Reserved, Sapling Data Inc, https://saplingdata.com
#
# Licensed under the MIT License (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is in the "LISENSE" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

__author__ = "mtruchard"

import re


def to_loki_date(date):
    """ Returns a date in YYYY-MM-DD format. """
    if date == '':
        return "0000-00-00"
    else:
        chunked = date.split('/')
        for i, chunk in enumerate(chunked):
            if len(chunk) == 1:
                chunked[i] = '0' + chunk
        if len(chunked[2]) == 2:
            formatted = '-'.join(['20' + chunked[2], chunked[0], chunked[1]])
        else:
            formatted = '-'.join([chunked[2], chunked[0], chunked[1]])
        return formatted


def to_number(text):
    """ Returns the converted decimal value or a value of None for input strings. """

    # Return the value of None for any text that is null or set to 'Not Applicable'
    if text == '' or 'Not Applicable' in text or 'not applicable' in text or text is None:
        return None

    # Evaluate only the second block of text following the '|' for fields like: "$6850 per person | $13700 per group"
    if '|' in text:
        text = text.split('|')[1]

    # Return the converted decimal value matched by regex.
    pattern = '[\\$]?[-+]?[\\$]?([0-9,]+)(\\.([0-9,]+))?([eE][-+]?([0-9,]+))?'
    match = re.search(pattern, text)

    # Return the value of None if no decimal value is matched by regex.
    if match is None:
        result = None
    else:
        result = match.group(1).replace(',', '')

    return result


def to_none(field):
    """ Returns the value of None for input empty strings and empty lists. """
    if field == '' or field == []:
        return None
    else:
        return field
