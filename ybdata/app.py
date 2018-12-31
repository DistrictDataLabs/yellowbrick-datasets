# ybdata.app
# CLI utility for executing yellowbrick dataset management commands.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 07:19:34 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: app.py [] benjamin@bengfort.com $

"""
CLI utility for executing yellowbrick dataset management commands.
"""

##########################################################################
## Imports
##########################################################################

from commis import color
from commis import ConsoleProgram

from .commands import COMMANDS
from .version import get_version


##########################################################################
## Console Program
##########################################################################

DESCRIPTION = "Yellowbrick dataset management utilties"
EPILOG      = "Intended for use by Yellowbrick maintainers and core contributors"


class YBDatasetUtility(ConsoleProgram):

    description = color.format(DESCRIPTION, color.CYAN)
    epilog      = color.format(EPILOG, color.MAGENTA)
    version     = color.format("v{}", color.CYAN, get_version(short=True))

    @classmethod
    def load(klass, commands=COMMANDS):
        utility = klass()
        for command in commands:
            utility.register(command)
        return utility