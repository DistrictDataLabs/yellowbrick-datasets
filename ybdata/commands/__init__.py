# ybdata.commands
# Subcommand definitions executed by the utility program.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 07:23:45 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Subcommand definitions executed by the utility program.
"""

##########################################################################
## Imports
##########################################################################

from .validate import ValidateCommand
from .convert import ConvertCommand
from .package import PackageCommand
from .upload import UploadCommand
from .list import ListCommand


##########################################################################
## Active Commands
##########################################################################

# Commands become available to the command-line if added to this list.
COMMANDS = [
    ValidateCommand, ConvertCommand, PackageCommand, UploadCommand, ListCommand
]