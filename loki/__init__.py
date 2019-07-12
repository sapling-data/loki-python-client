#
# Copyright (c) 2019 All Rights Reserved, SaplingData LLC, http://saplingdata.com
#
# Licensed under the MIT License (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is in the "LISENSE" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
# import ConfigParser import RawConfigParser

__author__ = "mtruchard"

import configparser
import os
from loki.urn import Urn
from loki.data import Data


class Loki:
    def __init__(self, config_file_name):
        config_file_name = os.path.expanduser(config_file_name)
        if not os.path.isfile(config_file_name):
            """FileNotFoundError"""
            raise Exception("File not found: "+config_file_name)

        config = configparser.RawConfigParser()
        self.properties = config.read(config_file_name)
        self._username = config.get('default', 'username')
        self._password = config.get('default', 'password')
        self._hosturl = config.get('default', 'hosturl')
        self.urn = Urn()
        self.data = Data(self)
