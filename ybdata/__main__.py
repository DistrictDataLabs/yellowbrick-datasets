# ybdata
# Entry point for CLI script used by python -m and setuptools.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 07:16:04 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: __main__.py [] benjamin@bengfort.com $

"""
Entry point for CLI script used by python -m and setuptools.
"""

##########################################################################
## Imports
##########################################################################

from .app import YBDatasetUtility


##########################################################################
## Main Method
##########################################################################

def main():
    """
    Loads the environment if required, loads the utility and executes it.
    """
    utility = YBDatasetUtility.load()
    utility.execute()


if __name__ == "__main__":
    main()