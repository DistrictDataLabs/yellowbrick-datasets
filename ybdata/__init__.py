# ybdata
# Yellowbrick datasets management and deployment scripts.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Dec 30 08:50:55 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Yellowbrick datasets management and deployment scripts.
"""

##########################################################################
## Imports
##########################################################################

# Import the version number at the top level
from .version import get_version, __version_info__

##########################################################################
## Package Version
##########################################################################

__version__ = get_version(short=True)