#!/usr/bin/python3

"""
This utilities class contain tools to support blockchain creation and maintenance
"""

import types

def is_list(data):
    suspect = data
    if isinstance(suspect,types.list):
        return True
