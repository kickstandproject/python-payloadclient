#!/usr/bin/env python

# Copyright (C) 2013 PolyBeacon, Inc.
#
# Author: Paul Belanger <paul.belanger@polybeacon.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from payloadclient import version


extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'payloadClient'
copyright = u'2013, Paul Belanger'
release = version.VERSION_INFO.version_string_with_vcs()
version = version.VERSION_INFO.canonical_version_string()
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
htmlhelp_basename = 'payloadclientdoc'

latex_elements = {
}

latex_documents = [
    ('index', 'payloadClient.tex', u'payload Client Documentation',
     u'Paul Belanger', 'manual'),
]

man_pages = [
    ('index', 'payloadClient', u'payload Client Documentation',
     [u'Paul Belanger'], 1)
]

texinfo_documents = [
    ('index', 'payloadClient', u'payload Client Documentation',
     u'Paul Belanger', 'payloadClient', 'One line description of project.',
     'Miscellaneous'),
]
