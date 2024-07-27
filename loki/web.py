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

import loki.utils


class Web:
    def __init__(self, loki):
        self.loki = loki

    def web_service_url(self, service_urn, /, *, subject_urn = None, urlParams = None):
        url = self.loki._hosturl + '/api/' + self.urn_to_url_path(service_urn)
        if subject_urn is not None:
            url = url + '/v/' + self.urn_to_url_path(subject_urn)
        params = ""
        for p in urlParams:
            v = urlParams[p]
            if v is not None:
                if params != "":
                    params = params + "&"
                params = params + p + "=" + v
        if params != "":
            url = url + "?" + params
        return url

    def urn_to_url_path(self, urn):
        """ Turns a urn into a path for a url """
        if urn is None:
            return None
        return urn.replace(":", "/")
