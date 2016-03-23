# Copyright 2016 - Alcatel-Lucent
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,  software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND,  either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from vitrage import clients
from vitrage.synchronizer.plugins.synchronizer_base import SynchronizerBase


class NovaBase(SynchronizerBase):
    def __init__(self, conf):
        super(NovaBase, self).__init__()
        self.client = clients.nova_client(conf)
        self.conf = conf

    def get_client(self):
        return self.client
