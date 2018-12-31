# ybdata.utils
# Helper functions for the ybdata utility.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 12:02:53 2018 -0500
#
# Copyright (C) 2019 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: utils.py [] benjamin@bengfort.com $

"""
Helper functions for the ybdata utility.
"""

##########################################################################
## Imports
##########################################################################

import os
import hashlib


##########################################################################
## Helper Functions
##########################################################################

def exists_in_dataset(root, *path):
    """
    Checks if the specified path (joined by os-specific sep) exists in the
    path specified by the root directory.
    """
    return os.path.exists(os.path.join(root, *path))


def sha256sum(path, blocksize=65536):
    """
    Computes the SHA256 signature of a file to verify that the file has not
    been modified in transit and that it is the correct version of the data.
    """
    sig = hashlib.sha256()
    with open(path, 'rb') as f:
        buf = f.read(blocksize)
        while len(buf) > 0:
            sig.update(buf)
            buf = f.read(blocksize)
    return sig.hexdigest()


def urljoin(*args):
    """
    Joins given arguments into an url. Trailing but not leading slashes are
    stripped for each argument.
    """
    return "/".join(map(lambda x: str(x).rstrip('/'), args))