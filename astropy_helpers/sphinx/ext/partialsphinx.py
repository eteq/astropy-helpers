# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import print_function

"""
This extension makes "partial" sphinx builds possible.
"""
import inspect
import os
import re
import sys

from docutils import nodes

from sphinx import addnodes


def source_read(app, docname, source):
    return
    if app.config.partial_build_mod:
        if app.config.partial_build_mod not in docname:
            print('skipping', docname)
            source[0] = ''
        else:
            print('including', docname)

def env_before_read_docs(app, env, docnames):
    1/0

def setup(app):
    app.add_config_value('partial_build_mod', '', 'env')

    app.connect('source-read', source_read)
    app.connect('env-before-read-docs', env_before_read_docs)
