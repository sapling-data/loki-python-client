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


def get_valid_segment(text):
    """ Returns None or the valid Loki-formatted urn segment for the given input string. """

    if text == '':
        return None
    else:
        # Return the converted text value with invalid characters removed.
        valid_chars = ['.', '_', '-']
        new_text = ''
        for char in text:
            if char in valid_chars or char.isalnum():
                new_text += char
        return new_text


def is_new(urn):
    """ returns the last segment of the given urn"""
    idx = urn.find("$");
    if idx >= 0 :
        return True
    else:
        return False


def is_resource_urn(urn):
    idx = urn.find("!");
    if idx >= 0 :
        return True
    else:
        return False


def get_last_segment(urn):
    """ Returns the last segment of the given urn """
    if urn is None:
        return None
        
    index = -1
    index1 = urn.rfind(":")
    index2 = urn.rfind("#")
    index3 = urn.rfind("!")
    if index1 > index2 and index1 > index3:
        index = index1
    elif index2 > index3:
        index = index2
    else:
        index = index3
        
    if index < 0:
        lastSegment = urn
    else:
        lastSegment = urn[index + 1:]
    return lastSegment


class Urn:
    """ def __init__(self): """

    def get_valid_segment(self,urn):
        return get_valid_segment(urn)

    def is_new(self,urn):
        return is_new(urn)

    def is_resource_urn(self,urn):
        return is_resource_urn(urn)

    def get_last_segment(self,urn):
        return get_last_segment(urn)
