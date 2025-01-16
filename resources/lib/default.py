# -*- coding: utf-8 -*-
#
# Copyright 2025 YourName or YourOrganization
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xbmc
import xbmcgui
import xbmcplugin
import os
from xbmcaddon import Addon

addon = Addon('script.idealkooks.searchpro')

def get_setting(id, default=None):
    """Helper function to retrieve settings from settings.xml."""
    return addon.getSetting(id) if addon.getSetting(id) else default

# Your code continues...
